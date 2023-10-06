#!/usr/bin/python3
"""A sript that start a Flask web application with some requirements"""
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import itemgetter


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database"""
    storage.close()


@app.route('/states_list')
def states_list():
    """Return list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lamda state: state.name)
    print(sorted_states)
    return render_template('states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
