#!/usr/bin/env python3
from flask import Flask, request


app = Flask(__name__)
@app.before_request
def do_smt():
    request.current_get = "I was here first"

@app.route('/')
def do_smt_next():
    return f"{request.current_get} and I was here after"

if __name__ == "__main__":
    app.run(debug=True)