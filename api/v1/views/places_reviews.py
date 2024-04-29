#!/usr/bin/python3
"""
Route for handling Review objects and operations
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.place import Place
from models.review import Review


@app_views.route("/places/<place_id>/reviews", methods=["GET"],
                 strict_slashes=False)
def reviews_by_place(place_id):
    """
    Retrieves all Review objects by place
    :param place_id: Place ID
    :return: JSON of all reviews
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    reviews = [review.to_json() for review in place.reviews]
    return jsonify(reviews)


@app_views.route("/places/<place_id>/reviews", methods=["POST"],
                 strict_slashes=False)
def review_create(place_id):
    """
    Create Review route
    :param place_id: Place ID
    :return: Newly created Review object
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    review_json = request.get_json(silent=True)
    if review_json is None:
        abort(400, 'Not a JSON')

    if "user_id" not in review_json:
        abort(400, 'Missing user_id')
    user_id = review_json["user_id"]
    if storage.get(User, user_id) is None:
        abort(404)

    if "text" not in review_json:
        abort(400, 'Missing text')

    review_json["place_id"] = place_id
    new_review = Review(**review_json)
    new_review.save()
    return jsonify(new_review.to_json()), 201


@app_views.route("/reviews/<review_id>", methods=["GET"],
                 strict_slashes=False)
def review_by_id(review_id):
    """
    Gets a specific Review object by ID
    :param review_id: Review ID
    :return: Review object with the specified ID or error
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    return jsonify(review.to_json())


@app_views.route("/reviews/<review_id>", methods=["PUT"],
                 strict_slashes=False)
def review_put(review_id):
    """
    Updates specific Review object by ID
    :param review_id: Review ID
    :return: Review object and 200 on success, or 400 or 404 on failure
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    review_json = request.get_json(silent=True)
    if review_json is None:
        abort(400, 'Not a JSON')

    for key, val in review_json.items():
        if key not in ["id", "created_at", "updated_at", "user_id",
                       "place_id"]:
            setattr(review, key, val)

    review.save()
    return jsonify(review.to_json())


@app_views.route("/reviews/<review_id>", methods=["DELETE"],
                 strict_slashes=False)
def review_delete_by_id(review_id):
    """
    Deletes Review by ID
    :param review_id: Review ID
    :return: Empty dictionary with 200 or 404 if not found
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    storage.delete(review)
    storage.save()
    return jsonify({}), 200
