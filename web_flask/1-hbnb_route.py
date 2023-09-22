#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask


app = Flask(__name__)

@app.route('/', strick_slashes=False)
def hello_hbnb():
    """Display home page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display hbnb page"""
    return "HBNB"


if __name__ == '__name__':
    app.run(host='0.0.0.0', port=500)
