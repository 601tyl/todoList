from flask import jsonify
from .response import make_response

# 处理400错误的函数
def handle_400(error):
    return make_response(400, message=error.description)

# 处理404错误的函数
def handle_404(error):
    return make_response(404, message="Resource not found")

# 处理500错误的函数
def handle_500(error):
    return make_response(500, message="Internal server error")