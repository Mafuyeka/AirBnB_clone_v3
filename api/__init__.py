#!/usr/bin/python3
"""
Initialize the API package
"""
from flask import Flask
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

from api.v1.views import *

app.register_blueprint(app_views)
