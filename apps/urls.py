#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2019-09-27 15:14
"""

from uuid import uuid4

from flask import jsonify, request, g, make_response
from werkzeug import exceptions

from apps import app

SUCCESS_MSG = app.config['SUCCESS_MSG'].copy()


@app.before_request
def api_before_request():
    g.request_id = request.headers.get('X-Request-Id', uuid4().get_hex())


@app.after_request
def append_request_id(response):
    response.headers.add('X-Request-Id', g.request_id)
    return response


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def heartbeat():
    return jsonify(SUCCESS_MSG)


# 全局路由错误
@app.errorhandler(exceptions.NotFound.code)
def not_found(error):
    return make_response(
        jsonify(
            {
                'message': 'URL not found.' or error.description,
                'result': False,
                'status': exceptions.NotFound.code,
            }
        ),
        exceptions.NotFound.code
    )


# 全局异常错误(DEBUG模式生效)
@app.errorhandler(Exception)
def exception(error):
    return make_response(
        jsonify(
            {
                'message': error.message or exceptions.InternalServerError.description,
                'result': False,
                'status': exceptions.InternalServerError.code,
            }
        ),
        exceptions.InternalServerError.code
    )

# 全局内部错误
# @app.errorhandler(500)
# def exception(error):
#     return make_response(
#         jsonify(
#             {
#                 'message': 'Internal server error.' or error.description,
#                 'result': False,
#                 'status': exceptions.InternalServerError.code,
#             }
#         ),
#         exceptions.InternalServerError.code
#     )
