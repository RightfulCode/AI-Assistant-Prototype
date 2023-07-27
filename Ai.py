from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3

engine = pyttsx3.init()

chatbot = ChatBot('Kisara')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')


def log(message,resp):
    with open("log.txt", "+a") as file:
        file.write(str(message) + "\n" + str(resp) + "\n")

def generate_response(message):
    response = chatbot.get_response(message)
    return response

if __name__ == "__main__":
    while True:
        action = input("You:").lower()
        resp = generate_response(action)
        print("Bot:" + str(resp))
        engine.say(resp)
        engine.runAndWait()