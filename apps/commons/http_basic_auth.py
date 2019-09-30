#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: http_basic_auth.py
@time: 2019-09-27 10:49
"""

from flask_httpauth import HTTPBasicAuth

from apps.commons.exceptions import Unauthorized
from config import current_config

basic_auth = HTTPBasicAuth()

BASIC_AUTH_USERNAME = current_config.BASIC_AUTH_USERNAME
BASIC_AUTH_PASSWORD = current_config.BASIC_AUTH_PASSWORD


@basic_auth.verify_password
def verify_password(username, password):
    # user = User.query.filter_by(username = username).first()
    # if not user or not user.verify_password(password):
    #     return False
    # g.user = user
    if username != BASIC_AUTH_USERNAME:
        raise Unauthorized(description='Username Error.')
    if password != BASIC_AUTH_PASSWORD:
        raise Unauthorized(description='Password Error.')
    return True

#
# @basic_auth.error_handler
# def unauthorized():
#     raise Unauthorized
