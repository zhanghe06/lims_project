#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: http_token_auth.py
@time: 2019-09-27 10:52
"""

from flask_httpauth import HTTPTokenAuth
from itsdangerous import SignatureExpired, BadSignature

from apps.commons.exceptions import TokenError, TokenExpired, TokenNotExist
from libs.auth_token import verify_auth_token

token_auth = HTTPTokenAuth(scheme='Bearer')


@token_auth.verify_token
def verify_token(token):
    if not token:
        raise TokenNotExist
    try:
        return verify_auth_token(token)
    except SignatureExpired:
        raise TokenExpired
    except BadSignature:
        raise TokenError
