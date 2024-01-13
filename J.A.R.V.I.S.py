import subprocess
import wolframalpha
import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import time
import requests
from random import choice
import json
import os
import winshell
import pyjokes
import pytz
import pywhatkit as kit
from playsound import playsound
import feedparser
import smtplib
import ctypes
import time
import shutil
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from replies import reply_text
'****************************************************************************'
# voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',230)

'****************************************************************************'
# user defined functions
def speak(audio):             #<------- Converts the text to speech. Speaks the audio(command)
        engine.say(audio)  
        engine.runAndWait()

def introduce():
        mp3File="E:/Coding/python/Jarvis.mp3"
        print("Intro audio running in background......")
        playsound(mp3File)

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
                speak("Good Morning Sir !")
                print("Good Morning Sir !")

        elif hour>= 12 and hour<18:
                speak("Good Afternoon Sir !")
                print("Good Afternoon Sir !")

        else:
                speak("Good Evening Sir !")
                print("Good Evening Sir !")

        assname =("Jarvis")
        speak("I am your Personal Assistant")
        speak(assname)
        print("I am your peronal Assistant",assname)
        

def usrname():
        speak("What should i call you sir")
        print("What should i call you sir")
        uname = takeCommand()
        speak("Welcome Mister")
        speak(uname)
        print("Welcome Mr."+uname)
        columns = shutil.get_terminal_size().columns
        
        print("#####################".center(columns))
        print("Welcome Mr.", uname.center(columns))
        print("#####################".center(columns))
        
        speak("How can i Help you, Sir")
        print("How can i Help you, Sir")

def takeCommand():
        
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=2)
                print("Listening...")
                r.pause_threshold = 0.8
                audio = r.listen(source)

        try:
                print("Recognizing...")
                query = r.recognize_google(audio, language ='en-in')
                print(f"User said: {query}\n")
                hour = int(datetime.datetime.now().hour)
                if 'exit' in query or 'stop' in query:
                        if hour>=21 and hour<6:
                                speak('Good night sir, take care!')
                                print('Good night sir, take care!')
                        else:
                                speak('Have a Good day sir!')
                                print('Have a Good day sir!')
                        exit()
        except Exception as e:
                print("Say that again please...")
                speak("Say that again please")
                return "None"
                
        return query

def play_on_youtube(video):
        kit.playonyt(video)

def search_on_google(query):
        kit.search(query)

def search_on_wikipedia(query):
        results = wikipedia.summary(query, sentences=2)
        return results


'***********************************************************************'
# main function
if __name__ == '__main__':
        clear = lambda: os.system('cls')
        
        clear()
        introduce()         # Introduction audio plays in the background
        wishMe()
        usrname()        

        
        while True:
                
                query = takeCommand().lower()
                
                # All the commands said by user will be
                # stored here in 'query' and will be
                # converted to lower case for easy
                # recognition of command
                if 'wikipedia' in query:                                         # Opens wikipedia
                        try:                                
                                speak('What do you want to search on Wikipedia, sir?')
                                search_query = takeCommand().lower()
                                results = search_on_wikipedia(search_query)
                                print(results)
                                speak(f"According to Wikipedia, {results}")
                        except Exception:
                                print("Say that again please")
                                speak("Say that again please")                      
                        
                        
                elif 'youtube' in query:                                         # Opens Youtube and plays the video as per our voice command 
                        speak('What do you want to play on Youtube, sir?')
                        video = takeCommand().lower()
                        play_on_youtube(video)
                        
                elif 'search on google' in query:                                # Opens Google and searches for the information as per our voice command
                        speak('What do you want to search on Google, sir?')
                        query = takeCommand().lower()
                        search_on_google(query)


                elif 'play music' in query or 'play song' in query:              # Opens Spotify Web player to play songs
                        print("Here you go to spotify")
                        speak("Here you go to spotify")
                        webbrowser.open('https://open.spotify.com/')

                elif 'drop my needle' in query:                                  # Music plays in the background
                        print("Playing your beat in the background.....")
                        playsound("E:\Coding\python\Vaathi Coming.mp3")
                        
                      
                elif 'the time' in query:                                        # Tells the time in IST format
                        timezone = pytz.timezone('Asia/Kolkata')
                        now = datetime.datetime.now(tz=timezone)
                        time = now.strftime("%H:%M:%S")
                        print("time:", time)
                        speak(f"Sir, the time is {time}")
                        
                elif 'the date' in query:                                        # Tells the date in IST format
                        timezone = pytz.timezone('Asia/Kolkata')
                        now = datetime.datetime.now(tz=timezone)
                        date= now.strftime("%m/%d/%Y")
                        print("date and time:",date)
                        speak(f"Sir, the date is {date}")
                        
                
                elif 'how are you' in query:
                        print("I am fine, Thank you")
                        print("How are you, Sir")
                        speak("I am fine, Thank you")
                        speak("How are you, Sir")

                elif 'fine' in query or "good" in query:
                        print("It's good to know that you are fine")
                        speak("It's good to know that you are fine")


                elif "change my name to" in query:
                        query = query.replace("change my name to", "")
                        uname = query

                elif "change name" in query:
                        speak("What would you like to call me, Sir ")
                        assname = takeCommand()
                        speak("Thanks for naming me")

                elif "what's your name" in query or "What is your name" in query:
                        print("My friends call me Jarvis")
                        speak("My friends call me Jarvis")                       


                elif "who made you" in query or "who created you" in query:
                        print("I was created by three students from SNP")
                        speak("I was created by three students from SNP")
                        
                
                elif 'joke' in query:                                           # Tells a joke
                        joke=pyjokes.get_joke()
                        print(joke)
                        speak(joke)
                        
                elif "calculate" in query:                                      # Performs simple and complex mathematical calculations
                        
                        app_id = "QLWVJW-QGKG672KL3"
                        client = wolframalpha.Client(app_id)
                        indx = query.lower().split().index('calculate')
                        query= query.split()[indx + 1:]
                        res = client.query(' '.join(query))
                        answer = next(res.results).text
                        print("The answer is " + answer)
                        speak("The answer is " + answer)

                elif 'search' in query or 'play' in query:                     # Searches on Google
                        
                        query = query.replace("search", "")
                        query = query.replace("play", "")               
                        search_on_google(query)

                elif "who am i" in query:
                        print("If you talk then definitely you are a human.")
                        speak("If you talk then definitely you are a human.")


                elif "who are you" in query:
                        print("I am Jarvis a virtual assistant, whose job is to help you use your computer in a more efficient way")
                        speak("I am Jarvis a virtual assistant, whose job is to help you use your computer in a more efficient way")

                elif 'your purpose' in query:
                        print("I am here to help you perform computer operations with just a voice command")
                        speak("I am here to help you perform computer operations with just a voice command")

                elif 'news' in query:                                          # Tells the current news
                        
                        news_headlines = []
                        res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=0838bfa2682040bb8eca480df8bc8f71 &category=general").json()
                        articles = res["articles"]
                        for i in range(0,5):
                                news_headlines.append(articles[i]['title'])
                        print(*news_headlines, sep="\n\n")
                        speak(news_headlines)

                elif "weather" in query:                                       # Tells the current weather forecast
                        
                        res=requests.get("http://api.openweathermap.org/data/2.5/weather?q=chennai&appid=70fec8d38cfbe3f2cc3935ede42d101f&units=metric").json()
                        weather = res["weather"][0]["main"]
                        temperature = res["main"]["temp"]
                        feels_like = res["main"]["feels_like"]
                        pressure=res["main"]["pressure"]
                        print(" Temperature (in kelvin unit) = " +str(temperature)+"\n atmospheric pressure (in hPa unit) ="+str(pressure) +"\n description = " +str(weather))
                        speak(f"The current temperature is {temperature},But it feels like {feels_like}")
                        speak(f"Also the weather reports describes {weather}")
                                                      
                elif 'shutdown protocol' in query:                             #  Shutdowns the system
                                speak("Initiating shut down protocol. All systems going offline!")
                                os.system("shutdown /s /t 1")
                                

                elif "where is" in query:                                      # Opens Google map
                        
                        query = query.replace("where is", "")
                        location = query
                        speak("User asked to Locate")
                        speak(location)
                        print("User asked to Locate -",location)
                        webbrowser.open("https://www.google.co.in/maps/place/" + location + "")


                elif "restart" in query:                                       # Restarts the system                                  
                        speak("rebooting all systems")
                        print("rebooting all systems")
                        os.system("shutdown /r /t 1")
                        
                        
                elif "hibernate" in query or "sleep" in query:                 # Hibernates the system
                        speak("I am going to sleep sir. Goodbye! ")
                        subprocess.call("shutdown /h")

                elif "log off" in query or "sign out" in query:                # Signs out of the system 
                        speak("Make sure all the application are closed before sign-out")
                        time.sleep(5)
                        subprocess.call(["shutdown", "/l"])

                elif "don't listen" in query or "pause" in query :             # Stops listening for the specified seconds
                        
                        print("For how much time you want to stop jarvis from listening commands")
                        speak("For how much time you want to stop jarvis from listening commands")
                        t = int(takeCommand())
                        time.sleep(t)
                        print("I am back sir!")
                        speak("I am back sir!")
                                        
                elif "jarvis are you up" in query:
                        print("For you sir, always")
                        speak("For you sir, always")
                        
                        
                elif "jarvis are you there" in query:
                        print("At your service, sir")
                        speak("At your service, sir")
                        

                elif "morning" in query:
                        print("A warm morning")
                        print("How are you Sir?")
                        speak("A warm morning")
                        speak("How are you Sir?")
                        


                elif "what is" in query or "who is" in query:                    # Searches from information from Wolframalpha data

                        client = wolframalpha.Client("QLWVJW-QGKG672KL3")
                        res = client.query(query)
                        
                        try:
                                print (next(res.results).text)
                                speak (next(res.results).text)
                        except StopIteration:
                                print ("No results")

#*************************************Thank you*************************************************




