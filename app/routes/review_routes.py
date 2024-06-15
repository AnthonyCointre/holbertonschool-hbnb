#!/usr/bin/env python3

from flask import Blueprint, request, jsonify, current_app
import uuid
from datetime import datetime

review_bp = Blueprint('review_bp', __name__)


@review_bp.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data_manager_review = current_app.config['DATA_MANAGER_REVIEW']
    data_manager_user = current_app.config['DATA_MANAGER_USER']
    data_manager_place = current_app.config['DATA_MANAGER_PLACE']
    data = request.get_json()

    required_fields = ['user_id', 'rating', 'comment']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field.capitalize()} is required'}), 400

    user_id = data['user_id']
    rating = data['rating']
    comment = data['comment'].strip()

    user = next(
        (u for u in data_manager_user.data if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    place = next(
        (p for p in data_manager_place.data if p['id'] == place_id), None)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    if user['id'] == place['host_id']:
        return jsonify({'error': 'Hosts cannot review their own places'}), 400

    new_review = {
        "id": str(uuid.uuid4()),
        "place_id": place_id,
        "user_id": user_id,
        "rating": rating,
        "comment": comment,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    data_manager_review.data.append(new_review)
    data_manager_review.save()

    return jsonify(new_review), 201


@review_bp.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    data_manager_review = current_app.config['DATA_MANAGER_REVIEW']
    reviews = [r for r in data_manager_review.data if r['user_id'] == user_id]
    return jsonify(reviews), 200


@review_bp.route('/places/<place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    data_manager_review = current_app.config['DATA_MANAGER_REVIEW']
    reviews = [r for r in data_manager_review.data if r['place_id'] == place_id]
    return jsonify(reviews), 200


@review_bp.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    data_manager_review = current_app.config['DATA_MANAGER_REVIEW']
    review = next(
        (r for r in data_manager_review.data if r['id'] == review_id), None)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review), 200


@review_bp.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data_manager_review = current_app.config['DATA_MANAGER_REVIEW']
    data = request.get_json()

    review = next(
        (r for r in data_manager_review.data if r['id'] == review_id), None)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    if 'rating' in data:
        review['rating'] = data['rating']
    if 'comment' in data:
        review['comment'] = data['comment'].strip()

    review['updated_at'] = datetime.now().isoformat()
    data_manager_review.save()

    return jsonify(review), 200


@review_bp.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    data_manager_review = current_app.config['DATA_MANAGER_REVIEW']
    review = next(
        (r for r in data_manager_review.data if r['id'] == review_id), None)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    data_manager_review.data = [
        r for r in data_manager_review.data if r['id'] != review_id]
    data_manager_review.save()

    return '', 204
