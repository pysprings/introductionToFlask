# -*- coding: utf-8 -*-
"""
    Firstapp
    ~~~~~~

    A trivial Flask Example

    :copyright: (c) 2012 by Tim Flink, some content borrowed from Flaskr
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, request, redirect, url_for, render_template

# configuration
DEBUG = True

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# render a simple template for the base
@app.route('/')
def show_index():
    return render_template('index.html')

# Render a page using variables set statically
@app.route('/fruit')
def show_fruit():
    myfruit = ['Apples', 'Banannas', 'Strawberries', 'Mangos']
    return render_template('fruit.html', fruits=myfruit)

if __name__ == '__main__':
    app.run()
