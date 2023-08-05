from flask import Flask, render_template,request,redirect
import nltk


#chatbot code
from nltk.chat.util import Chat,reflections

rules=[(r"hello",["hi","hello"]),
       (r"ac is not working",["Pankha chalao","hmare yaha esa hi hota hai"])]

my_chat_bot= Chat(rules)

#flask code

app = Flask(__name__)

@app.route('/')
def home():
    return "home page yaha hai"

@app.route('/chat',methods=['POST','GET'])
def chatbot():
    #res=""
    if request.method == "POST":
        ques=request.form['ask_me']
        res=my_chat_bot.respond(ques)
        print(res)
        return render_template("chatbot.html",response_from_flask=res)
    else:
        return render_template("chatbot.html")
    
app.run(debug=True)
#debug=true means apne app server pe changes ho jaenge reload krne pr
