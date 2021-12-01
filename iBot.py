from flask import Flask, request
import requests
from gingerit.gingerit import GingerIt
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
chatbot = ChatBot('iBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")

@app.route('/bot', methods=['POST'])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    incomingMsg = request.values.get('Body', '').lower()
    parser = GingerIt()
    co = parser.parse(str(incomingMsg))
    correctedRes = co.get("result")
    res = chatbot.get_response(str(correctedRes))
    msg.body(str(res))
    responded = True
    return str(resp)

if __name__ == '__main__':
    app.run()
