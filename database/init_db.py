import os
from app.models.todo import Todo
from app import create_app, db


def initialize_database():
    # 创建应用实例
    app = create_app()

    with app.app_context():
        # 创建数据库目录（如果不存在）
        instance_path = app.instance_path
        if not os.path.exists(instance_path):
            os.makedirs(instance_path)
            print(f"Created instance folder at: {instance_path}")

        # 创建数据库表
        try:
            db.create_all()
            print("Database tables created successfully!")

            # 可选：添加初始测试数据
            if not Todo.query.first():
                initial_todos = [
                    Todo(title="学习Flask", description="完成REST API教程"),
                    Todo(title="购买杂货", completed=True),
                    Todo(title="锻炼身体")
                ]
                db.session.bulk_save_objects(initial_todos)
                db.session.commit()
                print("Added initial test data!")

        except Exception as e:
            print(f"Error creating database: {str(e)}")
            db.session.rollback()


if __name__ == '__main__':
    initialize_database()