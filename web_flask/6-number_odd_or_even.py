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


@app.route('/number/<n>')
def is_number(n):
    try:
        num = int(n)
        return "{} is a number".format(num)
    except ValueError:
        abort(404)


@app.route('/number_template/<n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def is_odd_or_even(n):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, is_odd=False)
    else:
        return render_template('6-number_odd_or_even.html', n=n, is_odd=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
