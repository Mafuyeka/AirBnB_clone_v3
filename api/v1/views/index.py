#!/usr/bin/python3
"""
View for the status endpoint
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """
    Return the status of the application
    """
    return jsonify({"status": "OK"})
