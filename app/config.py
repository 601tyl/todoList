import os
from dotenv import load_dotenv

load_dotenv()  # 加载环境变量

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///todos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    JSON_SORT_KEYS = False  # 保持JSON响应字段顺序