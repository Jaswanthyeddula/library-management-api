from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.library_service import (
    get_all_books,
    create_new_book,
    delete_book,
    get_one_book,
    update_book
)
book_bp = Blueprint('books', __name__)
@book_bp.route('/books', methods = ['GET'])
@jwt_required() # protected
def get_books():
    return jsonify(get_all_books())
@book_bp.route('/books', methods = ['POST'])
def add_book():
    data = request.get_json(force=True)
    return jsonify(create_new_book(data)), 201
@book_bp.route('/books/<int:id>', methods = ['DELETE'])
def remove_book(id):
    result = delete_book(id)
    if not result:
        return jsonify("not found")
    return jsonify(result)
@book_bp.route('/books/<int:id>', methods = ['GET'])
def one_book(id):
    answer = get_one_book(id)
    if not answer:
        return jsonify("not found")
    return jsonify(answer)
@book_bp.route('/books/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def modify_book(id):
    data = request.get_json(force=True)
    result = update_book(id, data)
    if not result:
        return jsonify({"error":"not found"})
    return jsonify(result)