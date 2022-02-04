import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime #pip install datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os
import smtplib #pip install smtplib
from word2number import w2n #pip install word2number


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



def calculate():  # Define our function

    speak("Please speak the math operation you would like to complete addition subtraction multiplication division")
    operation = takeCommand().lower()

    speak("speak first number")
    n1 = takeCommand().lower()
    number_1 = w2n.word_to_num(n1)

    speak("speak second number")
    n2 = takeCommand().lower() 
    number_2 = w2n.word_to_num(n2)

    if 'addition' in operation:
        Result = number_1 + number_2
        speak(Result)

    elif 'subtraction' in operation:
        Result = number_1 - number_2
        speak(Result)

    elif 'multiplication' in operation::
        Resultt = number_1 * number_2
        speak(Result)

    elif 'division' in operation:
        Result = number_1 / number_2
        speak(Result)

    else:
        speak("You have not speak a valid operator please speak a valid operator")

calculate()  # Call calculate() outside of the function


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open calculator' in query:
            calculate()
