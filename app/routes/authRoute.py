# auth.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app import db
from app.models import User

bp = Blueprint('authRoute', __name__)

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify({'token': access_token})
