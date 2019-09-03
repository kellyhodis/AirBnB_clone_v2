#!/usr/bin/python3
""" This is a script that starts a Flask web application.
    Listening on 0.0.0.0
    - port 5000
"""


from flask import abort, render_template, Flask
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


@app.route('/number/<n>')
def display_int(n=None):
    ''' Function to print '<n> is a number'
    '''
    try:
        int(n)
        return str(n) + ' is a number'
    except ValueError:
        abort(404)


@app.route('/number_template/<n>')
def display_html(n=None):
    ''' Function to print HTML page if n is integer
    '''
    try:
        int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        abort(404)


@app.route('/number_odd_or_even/<n>')
def display_html_odd_even(n=None):
    ''' Function to print HTML page if n is integer, and
    indicate whether odd or even
    '''
    try:
        int(n)
        if int(n) % 2 == 0:
            return render_template('6-number_odd_or_even.html',
                                   n=n, evenodd='even')
        else:
            return render_template('6-number_odd_or_even.html',
                                   n=n, evenodd='odd')
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run()
