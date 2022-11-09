from flask import Flask, request
import requests
from gingerit.gingerit import GingerIt
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# app = Flask(__name__)
chatbot = ChatBot('iBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
# trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.Insur")

# @app.route('/bot', methods=['POST'])
def bot():
    # resp = MessagingResponse()
    # msg = resp.message()
    # responded = False
    # res = chatbot.get_response(request.values.get('Body', '').lower())
    # msg.body(str(res))
    # responded = True
    # return str(resp)
    inp = input("Input: ")
    print("Output: " + str(chatbot.get_response(inp)))

# if __name__ == '__main__':
#     app.run()
while(True):
    bot()