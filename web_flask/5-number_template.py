#!/usr/bin/python3
"""Starts a flask web application."""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def C_text(text):
    f_text = text.replace('_', ' ')
    return "C {}".format(f_text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def py_text(text):
    f_text = text.replace('_', ' ')
    return "Python {}".format(f_text)


@app.route('/number/<int:n>')
def is_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
