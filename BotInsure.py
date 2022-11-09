# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# chatbot = ChatBot('insureBot')
# chatbot.storage.drop()
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")
# trainer.train("chatterbot.corpus.english.Insur")


# def bot():
#     inp = input("Input: ")
#     print("Output: " + str(chatbot.get_response(inp)))

# while(True):
#     bot()


from flask import Flask, render_template, request
from chatterbot import ChatBot
from gingerit.gingerit import GingerIt
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
#create chatbot
chatbot = ChatBot('insureBot')
chatbot.storage.drop()
trainer = ChatterBotCorpusTrainer(chatbot)
chatbot.storage.drop()
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.Insur")

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def bot():
    parser = GingerIt()
    inp = request.args.get('msg')
    co = parser.parse(str(inp.lower()))
    correctedRes = co.get("result")
    return str(chatbot.get_response(correctedRes))

if __name__ == "__main__":
    # while(True):
    app.run()