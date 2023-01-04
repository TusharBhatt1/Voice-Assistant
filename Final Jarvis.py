from os import startfile #Open file
import pyttsx3 #To convert text into speech
import speech_recognition as sr #Speech to text
import webbrowser as web #Open a link
import pyaudio #To record audio on windows
import wikipedia 
import datetime
import os #Operating system
print("--------------------*WELCOME*---------------------")
def printspeak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[2].id)
    engine.say(text)
    print(text)
    engine.runAndWait()

def intro():
    printspeak("Hello, I am designed by Mr. Tushar Bhatt. My name is Jarvis")
    printspeak("What's your name ?")    
intro()    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        print("Listening...")
        speech=r.recognize_google(audio)
        print("Recognizing...")

        try:
            printspeak(speech)
        except:
            printspeak("Try again")
            takecommand()
    return speech        
   

def uname():
    username=takecommand()
    printspeak(f"Hello {username}, tell me how may I help you ?")
    return username
uname=uname()

def query():
    while True:
        query=takecommand()
        query=query.tolower()
        if "Tushar" in uname and "who is my forever love" in query:
             printspeak("Tushar your forever love is the most beautiful girl in side out, Ms. Ankita  Ojha  to  be  Mrs. Ankita Tushar Bhatt soon")
             printspeak("You love Her the mostttttttttttt")
             printspeak("Happiness and foreverness to You beautiful Couple .")
             printspeak(" AT forever ")
             print("-----------------------------------------------------------------------------------------------------------------------------------")
             break

        elif "open google" in query:
            web.open_new_tab("www.google.com")
        elif "open youtube" in query:
            web.open_new_tab("www.youtube.com")
        elif "wikipedia" in query:
              query= query.replace("wikipedia"," ") 
              printspeak("According to qikipedia: ")
              printspeak(wikipedia.summary(query,sentences=4))
        elif "date" or "time" in query:
            result=datetime.datetime.now()
            printspeak(f"Here it is {result}")
        elif "open facebook" in query:
            web.open_new_tab("www.facebook.com")
        elif "open instagram" in query:
            web.open_new_tab("www.instagram.com")     
        elif "open vs code" in query:
            path="C:\\Users\\Tushar Bhatt\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            printspeak("Okay wait.")
            os.startfile(path)
        elif "exit" in query:
            break 
        else: printspeak("Try again")   
query()