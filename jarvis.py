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
import smtplib # SMTP/ESMTP client class (module)
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
# 0 : david
# 1 : zira
engine.setProperty('voices',voices[0].id)

# text to speech
def speak(string):
    engine.say(string)
    print(string)
    engine.runAndWait()

# voice (from mic) to text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in")
            print(f"user said:{query}")
        except Exception as e:
            # speak("Sorry Sir, Say that again please...")
            speak("Sorry Sir, I am not able to understand your command")
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

if __name__ == "__main__":
    # speak("this is jarvis 1.0")
    # speak("Hello Sir")
    # take_command()
    # print("testing")
    wish()

    while True:

        query = take_command().lower()
        
        if "no thanks" in query:
            speak("Thank you Sir, have a hice day")
            sys.exit()
        
        elif "open notepad" in query:
            speak("sure")
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("Anything else?")
        
        elif "open command prompt" in query:
            speak("okay here you go")
            os.system("start cmd")
            speak("Anything else?")
        elif "open calendar":
            webbrowser.open("https://calendar.google.com/calendar/u/0/r")
            speak("Anything else?")
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
            speak("Anything else?")
        elif "play music" in query:
            speak("sure")
            music_dir = "C:\\Users\\Milan\\Music\\playlist1"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("Anything else?")
            # for song in songs:
            #     if song.endswith('.mp3'):
            #         os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            speak("wait a second")
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            speak("Anything else?")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            speak("Anything else?")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            speak("Anything else?")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("Anything else?")
        
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")
            speak("Anything else?")
        elif "send message" in query:
            pywhatkit.sendwhatmsg("")
            speak("Anything else?")

        # elif "play songs on youtube" or "songs on youtube" in query:
        #     speak("OK, which song?")
        #     songname = take_command().lower()
        #     pywhatkit.playonyt(songname)
        #     speak("Anything else?")

        elif "send email" in query:
            try:
                speak("OK, Please tell me the message you want to send")
                msg = take_command().lower()
                sender_email = "mcoinam01@gmail.com"
                password= "tech100business"
                receiver_email = "dhrubitaoinam888@gmail.com"
                
                server = smtplib.SMTP("smtp.gmail.com",587)
                server.starttls() # Puts the connection to the SMTP server into TLS mode
                server.login(sender_email, password)
                server.sendmail(sender_email,receiver_email,msg)
                speak("Email has been sent")
                speak("Do you have any other work for me?")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")
                speak("Anything else you want me to do?")
        else: # query is "none" or "some_unknown_string"
            speak("Say that again please")

       

            

        



