from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建扩展实例
db = SQLAlchemy()


def create_app():
    # 创建Flask应用实例
    app = Flask(__name__, instance_relative_config=True)

    # 加载配置
    app.config.from_object('app.config.Config')

    # 初始化扩展
    db.init_app(app)

    # 注册蓝图
    from app.routes.todo_routes import todo_bp
    app.register_blueprint(todo_bp)

    # 注册错误处理器
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    from app.utils.errors import handle_400, handle_404, handle_500

    app.register_error_handler(400, handle_400)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(500, handle_500)