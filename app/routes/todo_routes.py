from flask import Blueprint, request
from app import db
from app.models.todo import Todo
from app.utils.response import make_response
from datetime import datetime

todo_bp = Blueprint('todos', __name__, url_prefix='/todos')


# ------------------------- 获取所有待办事项 -------------------------
@todo_bp.route('/', methods=['GET'])
def get_all_todos():
    try:
        todos = Todo.query.order_by(Todo.created_at.desc()).all()
        return make_response(200, "Success", [todo.to_dict() for todo in todos])
    except Exception as e:
        return make_response(500, f"Server error: {str(e)}")


# ------------------------- 获取单个待办事项 -------------------------
@todo_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    try:
        todo = Todo.query.get(todo_id)
        if not todo:
            return make_response(404, "Todo not found")
        return make_response(200, "Success", todo.to_dict())
    except Exception as e:
        return make_response(500, f"Server error: {str(e)}")


# ------------------------- 创建待办事项 -------------------------
@todo_bp.route('/', methods=['POST'])
def create_todo():
    # 验证请求数据
    if not request.is_json:
        return make_response(400, "Request must be JSON format")

    data = request.get_json()
    if 'title' not in data or not data['title'].strip():
        return make_response(400, "Title is required")

    try:
        # 创建新事项
        new_todo = Todo(
            title=data['title'].strip(),
            description=data.get('description', '').strip(),
            completed=data.get('completed', False)
        )

        db.session.add(new_todo)
        db.session.commit()

        return make_response(201, "Todo created", new_todo.to_dict())
    except Exception as e:
        db.session.rollback()
        return make_response(500, f"Create failed: {str(e)}")


# ------------------------- 更新待办事项 -------------------------
@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    # 验证请求数据
    if not request.is_json:
        return make_response(400, "Request must be JSON format")

    data = request.get_json()
    try:
        todo = Todo.query.get(todo_id)
        if not todo:
            return make_response(404, "Todo not found")

        # 更新字段
        if 'title' in data:
            if not data['title'].strip():
                return make_response(400, "Title cannot be empty")
            todo.title = data['title'].strip()

        if 'description' in data:
            todo.description = data['description'].strip()

        if 'completed' in data:
            if not isinstance(data['completed'], bool):
                return make_response(400, "Completed must be boolean")
            todo.completed = data['completed']

        todo.updated_at = datetime.utcnow()
        db.session.commit()

        return make_response(200, "Update success", todo.to_dict())
    except Exception as e:
        db.session.rollback()
        return make_response(500, f"Update failed: {str(e)}")


# ------------------------- 删除待办事项 -------------------------
@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:
        todo = Todo.query.get(todo_id)
        if not todo:
            return make_response(404, "Todo not found")

        db.session.delete(todo)
        db.session.commit()
        return make_response(200, "Delete success")
    except Exception as e:
        db.session.rollback()
        return make_response(500, f"Delete failed: {str(e)}")