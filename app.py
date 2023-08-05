from flask import Flask,render_template,request,redirect
import nltk
from nltk.chat.util import Chat,reflections
rules=[
    # in the form of tuple
    (r"hello",["hi","hello"]),
    (r"AC is not working",["fan on karlo","humare yha esa hi hota h"])
]

my_chat_bot=Chat(rules)

app=Flask(__name__)

@app.route('/')
def home():
    return "Home Page is here"


@app.route('/chat',methods = ['POST','GET'])
def chatbot():
    if request.method=="POST":
        ques=request.form["ask me"]
        res=my_chat_bot(ques)
        print(res)
    return render_template("aap2.html")




app.run(debug= True)