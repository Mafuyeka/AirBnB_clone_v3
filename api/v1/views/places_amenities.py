#!/usr/bin/python3
"""
Route for handling place and amenities linking
"""
from flask import jsonify, abort, request
from os import getenv
from api.v1.views import app_views, storage
from models.place import Place
from models.amenity import Amenity


@app_views.route("/places/<place_id>/amenities", methods=["GET"],
                 strict_slashes=False)
def amenity_by_place(place_id):
    """
    Get all amenities of a place
    :param place_id: Place ID
    :return: All amenities
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    amenities = [amenity.to_json() for amenity in place.amenities]
    return jsonify(amenities)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=["DELETE"], strict_slashes=False)
def unlink_amenity_from_place(place_id, amenity_id):
    """
    Unlink an amenity from a place
    :param place_id: Place ID
    :param amenity_id: Amenity ID
    :return: Empty dictionary or error
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    if amenity not in place.amenities:
        abort(404)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        place.amenities.remove(amenity)
    else:
        place.amenity_ids.remove(amenity.id)

    place.save()
    return jsonify({}), 200


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 methods=["POST"], strict_slashes=False)
def link_amenity_to_place(place_id, amenity_id):
    """
    Link an amenity with a place
    :param place_id: Place ID
    :param amenity_id: Amenity ID
    :return: Amenity object added or error
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    if amenity in place.amenities:
        return jsonify(amenity.to_json()), 200

    if getenv("HBNB_TYPE_STORAGE") == "db":
        place.amenities.append(amenity)
    else:
        place.amenity_ids.append(amenity.id)

    place.save()
    return jsonify(amenity.to_json()), 201
