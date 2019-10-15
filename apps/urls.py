#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2019-09-27 15:14
"""

from __future__ import unicode_literals

from uuid import uuid4

from flask import jsonify, request, g, make_response
from werkzeug.exceptions import NotFound, InternalServerError
from apps.signals.operation_log import signal_operation_log
from apps import app

SUCCESS_MSG = app.config['SUCCESS_MSG'].copy()


@app.before_request
def api_before_request():
    g.request_id = request.headers.get('X-Request-Id', str(uuid4()))  # 不带短横: uuid4().get_hex()


@app.after_request
def append_request_id(response):
    # 头部注入
    response.headers.add('X-Request-Id', g.request_id)

    # 操作日志
    if request.method in ['POST', 'PUT', 'DELETE']:
        operation_log = {
            'req_method': request.method,
            'req_path': request.path,
            'req_json': request.json,
            'req_view_args': request.view_args,
            'res_status_code': response.status_code,
        }
        signal_operation_log.send(app, **operation_log)
    return response


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def heartbeat():
    return jsonify(SUCCESS_MSG)


# 全局路由错误
@app.errorhandler(NotFound.code)
def url_not_found(error):
    return make_response(
        jsonify(
            {
                'message': '路径错误' or error.description,
                'result': False,
                # 'status': exceptions.NotFound.code,
            }
        ),
        NotFound.code
    )


# 全局异常错误(DEBUG模式生效)
@app.errorhandler(Exception)
def exception(error):
    return make_response(
        jsonify(
            {
                'message': error.message or InternalServerError.description,
                'result': False,
                # 'status': InternalServerError.code,
            }
        ),
        InternalServerError.code
    )
