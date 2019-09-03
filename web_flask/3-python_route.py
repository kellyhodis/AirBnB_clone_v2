#!/usr/bin/python3
""" This is a script that starts a Flask web application.
    Listening on 0.0.0.0
    - port 5000
"""


from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    ''' Function to print 'Hello HBNB!'
    '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    ''' Function to print 'HBNB'
    '''
    return 'HBNB'


@app.route('/c/<text>')
def display(text):
    ''' Function to print 'C' followed by user input
    '''
    return 'C ' + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    ''' Function to print 'Python' followed by user input
    '''
    return 'Python ' + text.replace("_", " ")


if __name__ == "__main__":
    app.run()
