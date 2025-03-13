from flask import jsonify

def make_response(code, message=None, data=None):
    """统一响应格式生成器"""
    response = {
        'code': code,
        'msg': message,
        'data': data
    }
    return jsonify(response), code