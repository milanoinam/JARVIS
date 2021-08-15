import pyttsx3 
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
# 0 : david
# 1 : zira
engine.setProperty('voices',voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# voice (from mic) to text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said:{query}")
    except Exception as e:
        speak("Sorry Sir, Say that again please...")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning, Sir")
    elif hour>=12 and hour <= 18:
        speak("Good Afternoon, Sir")
    else:
        speak("Good Evening, Sir")
    speak("I am Jarvis. Please tell me how can I help you?")

def sendEmail(recipient_email,email_msg):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("mcoinam01@gmail.com","tech100business")
    server.sendmail(recipient_email,email_msg)


if __name__ == "__main__":
    # speak("this is advance jarvis")
    # speak("Hello Sir")
    # take_command()
    # print("testing")
    wish()
    
    # while True:
    if 1:
        
        query = take_command().lower()
        
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")
        
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        # elif "play music" in query:
        #     music_dir = ""
        #     songs = os.listdir(music_dir)
        #     # rd = random.choice(songs)
        #     # os.startfile(os.path.join(music_dir, rd))
           
        #     for song in songs:
        #         if song.endswith('.mp3'):
        #             os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        # open fb
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")

        # elif "send message" in query:
        #     pywhatkit.sendwhatmsg("")

        # elif "play songs on youtube" or "songs on youtube" in query:
        #     speak("OK, which song?")
        #     songname = take_command().lower()
        #     pywhatkit.playonyt(songname)

        elif "send email" or "email" in query:
            try:
                speak("Please tell me what should i say?")
                email_msg = take_command().lower()
                recipient_email = "dhrubitaoinam888@gmail.com"
                sendEmail(recipient_email,email_msg)
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")

        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day")
            sys.exit()

        speak("Sir, do you have any other work for me?")

            

        



