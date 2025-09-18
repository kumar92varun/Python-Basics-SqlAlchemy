from flask import Flask

app = Flask(__name__)

@app.get('/')
def homePage():
    return "Welcome, this is the home page"


