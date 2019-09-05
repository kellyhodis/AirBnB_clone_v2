#!/usr/bin/python3
""" This is a script that starts a Flask web application.
    Listening on 0.0.0.0
    - port 5000
"""


from models import State
from models import storage
from flask import abort, render_template, Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def display_states():
    ''' Display a HTML page with States
    '''
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(self):
    ''' Teardown
    '''
    storage.close()


if __name__ == "__main__":
    app.run()
