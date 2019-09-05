#!/usr/bin/python3
""" This is a script that starts a Flask web application.
    Listening on 0.0.0.0
    - port 5000
"""


from os import getenv
from models import State
from models import storage
from flask import abort, render_template, Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def display_cities_by_states():
    ''' Display a HTML page with Cities sorted by States
    '''
    states = storage.all("State")
    cities = storage.all("City")
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.teardown_appcontext
def tear_down(self):
    ''' Teardown
    '''
    storage.close()


if __name__ == "__main__":
    app.run()
