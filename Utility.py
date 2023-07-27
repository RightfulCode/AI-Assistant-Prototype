import webbrowser
import speech_recognition as sr
from googlesearch import search
import python_weather
import datetime
import subprocess
import pyttsx3
import wikipedia
import time
import asyncio

engine=pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty('rate')
engine.setProperty("voice",'english_rp+f3')
engine.setProperty("rate",rate-35)

def open_wiki(statement):
    speak('Searching Wikipedia...')
    statement =statement.replace("wikipedia", "")
    results = wikipedia.summary(statement, sentences=3)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def mute():
    speak("Entering mute mode")
    while True:
        statement = takeCommand(mute=True).lower()
        if "mute" in statement and "exit" in statement:
            break

def log_off():
    speak("Are you sure?")
    choice = takeCommand().lower()
    if "yes" in choice:
        speak("Shutting down your PC, good bye.")
        command = "shutdown -h now"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    else:
        speak("Returning to normal functionality")
        return

def weather():
    marker = True
    speak("Please specify the city")
    city = takeCommand().lower()
    if "quit" in city or "back" in city:
        marker = False
    if marker:
        try:
            temperature = asyncio.run(getweather(city))
            speak(f"The temperature in {city} is currently {temperature}")
        except:
            speak("Could not get temperature data, please ensure that you specified a valid city")
        

def open_utility(link,marker=False):
    webbrowser.open_new_tab(link)
    if marker:
        speak('Here are some headlines from the BBC, Happy reading')
    else:
        speak(f"{link} has been opened")
    time.sleep(5)

def open_link(array,dictionary):
    for i in array:
        try:
            number = int(i)
        except:
            pass
    if number:
        link = dictionary.get(number)
        try:
            webbrowser.open_new_tab(link)
        except:
            print("Link not found")
            print(dictionary)
    else:
        print("Please specify a number")
        speak("Please specify a number")

def google_search(query):
    def make_dict(key_list,value_list):
        sample = {key_list[i]:value_list[i] for i in range(len(key_list))}
        return sample
    link_address = []
    link_number = [x for x in range(1,11)]
    link_dict = dict({})
    control_variable = 10
    link_control_variable = 1
    for i in search(query,tld="co.in",num=10,stop=10,pause=2):
        print(f"{link_control_variable} {i}")
        link_address.append(i)
        link_control_variable += 1
    link_dict = make_dict(link_number,link_address)
    while True:
        link_control_variable = 1
        action = takeCommand().lower()
        if "next" in action:
            control_variable += 10
            link_dict.clear()
            link_address.clear()
            for i in search(query,tld="co.in", num=10,stop=10,pause=2,start=control_variable-10):
                print(f"{link_control_variable} {i}")
                link_address.append(i)
                link_control_variable += 1
            link_dict = make_dict(link_number,link_address)
        elif "previous" in action:
            if control_variable == 10:
                speak("Can't go further back.")
            else:
                control_variable -= 10
                link_dict.clear()
                for i in search(query,tld="co.in", num=10,stop=10,pause=2,start=control_variable-10):
                    print(f"{link_control_variable} {i}")
                    link_address.append(i)
                    link_control_variable += 1
                link_dict = make_dict(link_number,link_address)
        elif "open" in action:
            sep_statement = action.split()
            open_link(sep_statement,link_dict)
        else:
            break

async def getweather(city):
    async with python_weather.Client(unit=python_weather.METRIC,) as client:
        weather = await client.get(city)
    
        return weather.current.temperature

def takeCommand(mute=False):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            if mute:
                return "None"
            else:
                speak("Pardon me, please say that again")
                return "None"
        return statement
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def speak(text):
    engine.say(text)
    engine.runAndWait()