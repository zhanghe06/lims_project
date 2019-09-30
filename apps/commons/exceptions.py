#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: exceptions.py
@time: 2019-09-27 13:28
"""

from werkzeug.exceptions import (
    Unauthorized,
    Forbidden,
    Conflict,
    Gone,
    Locked,
    BadRequest,
    NotFound,
    MethodNotAllowed,
    PreconditionFailed,
    RequestEntityTooLarge,
    UnsupportedMediaType,
    InternalServerError,
    BadGateway,
    ServiceUnavailable,
)


# 自定义 TOKEN 异常
class TokenNotExist(Forbidden):
    description = 'Token required.'


class TokenExpired(Forbidden):
    description = 'Token expired.'


class TokenError(Forbidden):
    description = 'Token error.'


errors = {
    'Exception': {
        'message': 'Internal server error.',
        'result': False,
        'status': InternalServerError.code,
    },
    'BadRequest': {
        'message': 'Bad request.',
        'result': False,
        'status': BadRequest.code,
    },
    'Unauthorized': {
        'message': 'Authentication required.',
        'result': False,
        'status': Unauthorized.code,
    },
    'Forbidden': {
        'message': 'Forbidden.',
        'result': False,
        'status': Forbidden.code,
    },
    'TokenNotExist': {
        'message': 'Token required.',
        'result': False,
        'status': TokenNotExist.code or Forbidden.code,
    },
    'TokenExpired': {
        'message': 'Token expired.',
        'result': False,
        'status': TokenExpired.code or Forbidden.code,
    },
    'TokenError': {
        'message': 'Token error.',
        'result': False,
        'status': TokenError.code or Forbidden.code,
    },
    'NotFound': {
        'message': 'Resource not found.',
        'result': False,
        'status': NotFound.code,
    },
    'MethodNotAllowed': {
        'message': 'Method not allowed.',
        'result': False,
        'status': MethodNotAllowed.code,
    },
    'Conflict': {
        'message': 'Conflict, Resource already exists.',
        'result': False,
        'status': Conflict.code,
    },
    'Gone': {
        'message': 'Gone, Resource is gone.',
        'result': False,
        'status': Gone.code,
    },
    'Locked': {
        'message': 'Locked, Resource is locked.',
        'result': False,
        'status': Locked.code,
    },
    'PreconditionFailed': {
        'message': 'Precondition failed.',
        'result': False,
        'status': PreconditionFailed.code,
    },
    'RequestEntityTooLarge': {
        'message': 'Request entity too large.',
        'result': False,
        'status': RequestEntityTooLarge.code,
    },
    'UnsupportedMediaType': {
        'message': 'Unsupported media type.',
        'result': False,
        'status': UnsupportedMediaType.code,
    },
    'InternalServerError': {
        'message': 'Internal server error.',
        'result': False,
        'status': InternalServerError.code,
    },
    'BadGateway': {
        'message': 'Bad gateway.',
        'result': False,
        'status': BadGateway.code,
    },
    'ServiceUnavailable': {
        'message': 'Service unavailable.',
        'result': False,
        'status': ServiceUnavailable.code,
    },
}
