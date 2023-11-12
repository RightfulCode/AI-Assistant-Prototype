import Utility
import time
import datetime
from Ai import generate_response

if __name__=='__main__':

    Utility.wishMe()
    Utility.speak("How can I help you today?")
    while True:

        statement = Utility.takeCommand().lower()

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            Utility.speak('your personal assistant Kisara is shutting down, Good bye')
            print('your personal assistant Kisara is shutting down, Good bye')
            break

        elif 'wikipedia' in statement:
            Utility.open_wiki(statement)

        elif 'open youtube' in statement:
            Utility.open_utility("https://www.youtube.com")

        elif 'open google' in statement:
            Utility.open_utility("https://www.google.com")

        elif 'open gmail' in statement:
            Utility.open_utility("gmail.com")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            Utility.speak(f"the time is {strTime}")

        elif 'news' in statement:
            Utility.open_utility("https://www.bbc.com/news/world", marker=True)

        elif 'search'  in statement:    
            statement = statement.replace("search", "")
            Utility.google_search(statement)
            time.sleep(5)	

        elif 'who are you' in statement or 'what can you do' in statement:
            Utility.speak('I am designated as Kisara, version 7 point 8 personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail ,predict time,search wikipedia,' 
                  'get top headline news from times of india and you can ask me other general questions too!')

        elif "weather" in statement:
            Utility.weather()
                
        elif "log off" in statement or "sign out" in statement:
            Utility.log_off()

        elif "mute" in statement:
            Utility.mute()

        else:
            resp = str(generate_response(statement))
            Utility.speak(resp)
            print(resp)
