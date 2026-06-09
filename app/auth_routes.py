from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from app import bcrypt
auth_bp = Blueprint('auth',__name__)
users =[]
@auth_bp.route('/register',methods= ['POST'])
def register():
    data = request.get_json(force=True)
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    print("original", data['password'])
    print("hashed", hashed_password)
    user = {
        "username":data['username'],
        "password":hashed_password
    }
    users.append(user)
    return jsonify(hashed_password)
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    user = next((u for u in users
                 if u['username'] == data['username']), None)
                 
    if not user :
        return jsonify({"message":"user not found"}), 401
    if not bcrypt.check_password_hash(
        user['password'],
        data['password']
    ):
        return jsonify({"message":"wrong password"}), 401
    
    token = create_access_token(identity=data['username'])
    return jsonify({"token":token}), 200

    
                 
