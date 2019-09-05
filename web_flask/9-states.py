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


@app.route('/states')
@app.route('/states/<id>')
def display_state_id(id=None):
    ''' Display a specific State with id
    '''
    cities = storage.all("City")
    states = storage.all("State")
    return render_template('9-states.html', states=states,
                           cities=cities, id=id)


@app.teardown_appcontext
def tear_down(self):
    ''' Teardown
    '''
    storage.close()


if __name__ == "__main__":
    app.run()
