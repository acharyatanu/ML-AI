from flask import Flask

app=Flask(__name__)                          #  __name__   gives  __main__   if a python file is run than value is main but if imported not main

@app.route('/')                              #@ is a decorator in python that makes an funcn extraordinary means more functionalitues can ve added to a pre existing funcn
def sample():
    return 'kuch bhi sample'


@app.route('/new')
def new():
    return '<h1> This is Heading</h1>'




app.run(debug=True)                                   # will create a local server



