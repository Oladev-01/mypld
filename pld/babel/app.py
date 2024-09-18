#!/usr/bin/env python3
"""i18n session"""
from flask import Flask, render_template, request
from flask_babel import Babel

# render_template(custom_template)
# start of Config class
class Config:
    LANGUAGES = ["en", "fr", "de"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
# end of Config class

# instantiate the Flask app
app = Flask(__name__)
# instantiating Babel

# set up app config
app.config.from_object(Config)
# end of app config
# define the route
def get_locale() -> str:
    """return the users locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"]) # "en, fr, de"

babel = Babel(app, locale_selector = get_locale)
@app.route('/')
def index() -> str:
    """return html page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


