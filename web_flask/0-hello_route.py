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


if __name__ == "__main__":
    app.run()
