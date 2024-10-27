from flask import Flask
app = Flask(__name__) # __name__ is a special variable in Python that is the name of the module.

@app.route('/') # This is a decorator that creates a mapping between the URL and the function.
def hello_world():
    return "Hello, World!"

