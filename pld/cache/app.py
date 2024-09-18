#!/usr/bin/env python3

"""cache session"""
from flask import Flask, request, jsonify, render_template, redirect, url_for
from database import BaseCaching

database = BaseCaching()

app = Flask(__name__)


@app.route('/')
def add_cache():
    #implementing the FIFO cache
    fifo = request.args.get('fifo', None)
    data = database.print_cache()
    return render_template('cache.html', cache_data=data, fifo=fifo)

@app.route('/cache', methods=['POST'])
def update_cache():
    # Handle the POST request
    key = request.form['key']
    value = request.form['value']
    fifo = database.put(key, value)
    return redirect(url_for('add_cache', fifo=fifo))

@app.route('/cache/<key>', methods=['GET'])
def get_key(key):
    """get value by key"""
    if not key:
        return None
    return database.get(key)


if __name__ == '__main__':
    app.run(debug=True)