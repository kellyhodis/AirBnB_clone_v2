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


@app.route('/hbnb_filters')
def display_index():
    ''' Display a specific State with id
    '''
    cities = storage.all("City")
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def tear_down(self):
    ''' Teardown
    '''
    storage.close()


if __name__ == "__main__":
    app.run()
