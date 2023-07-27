import speech_recognition as sr
import pyttsx3
from googlesearch import search
import datetime
import wikipedia
import webbrowser
import time
import subprocess
import python_weather
import asyncio
from Ai import generate_response

engine=pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.getProperty('rate')
engine.setProperty("voice",'english_rp+f3')
engine.setProperty("rate",rate-35)

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
        #action = input("You:")
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
    
        print(weather.current.temperature)
        speak(f"The temeperature is around {weather.current.temperature}")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
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

if __name__=='__main__':

    wishMe()
    speak("How can I help you today?")
    while True:

        #statement = input("You:").lower()
        statement = takeCommand().lower()

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Kisara is shutting down, Good bye')
            print('your personal assistant Kisara is shutting down, Good bye')
            break

        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.bbc.com/news/world")
            speak('Here are some headlines from the BBC, Happy reading')
            time.sleep(6)

        elif 'search'  in statement:    
            statement = statement.replace("search", "")
            google_search(statement)
            time.sleep(5)	

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am designated as Kisara, version 7 point 8 personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail ,predict time,search wikipedia,' 
                  'get top headline news from times of india and you can ask me other general questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Syed Ali Raza Mehdi, also known as Rightful")
            print("I was built by Syed Ali Raza Mehdi, also known as Rightful")

        elif "weather" in statement:
            asyncio.run(getweather("bahawalpur"))
                
        elif "log off" in statement or "sign out" in statement:
            speak("Are you sure?")
            #statement = input("You:").lower()
            statement = takeCommand().lower()
            if "yes" in statement:
                speak("Shutting down your PC, good bye.")
                command = "shutdown -h now"
                process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            else:
                speak("Returning to normal functions")
        elif "mute" in statement:
            speak("Entering mute mode")
            while True:
                #statement = input("You:").lower()
                statement = takeCommand().lower()
                if "mute"in statement and "exit" in statement:
                    speak("Exitting mute mode")
                    break
        else:
            resp = str(generate_response(statement))
            speak(resp)
            print(resp)