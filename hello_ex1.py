# hello world
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"
# by this line hold or run our app
app.run()