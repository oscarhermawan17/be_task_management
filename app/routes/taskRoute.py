from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app import db
from app.models import User, Task

bp = Blueprint('taskRoute', __name__)

@bp.route('/', methods=['GET'])
def index():
    return 'Hello, Flask!', 200

@bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_task = Task(title=data['title'], description=data['description'], status=data['status'], user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_dict() for task in tasks])

@bp.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.status = data['status']
    db.session.commit()
    return jsonify(task.to_dict())

@bp.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=id, user_id=user_id).first()
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return '', 204
