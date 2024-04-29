from flask import Flask, Blueprint, jsonify

app_views = Blueprint('app_views', __name__)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})
