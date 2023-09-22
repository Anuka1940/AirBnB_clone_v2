#!/usr/bin/python3
"""this module concatinates two strings"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """returns c and text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text="is cool"):
    """returns python and text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """returns number and n"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """returns number and n"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_n(n):
    """returns number and n"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, odd_even="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, odd_even="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
