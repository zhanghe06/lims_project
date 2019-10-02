#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: default.py
@time: 2019-09-27 12:47
"""

from __future__ import print_function
from __future__ import unicode_literals

import binascii
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

HOST = '0.0.0.0'
PORT = 8000
DEBUG = False
SECRET_KEY = 'c9a6b2eb758aab3e1899576e76d72550cb3dd6d7a4b56b66'

# 意外异常捕获
PROPAGATE_EXCEPTIONS = True
PRESERVE_CONTEXT_ON_EXCEPTION = True

TOKEN_TTL = 600

# requests 超时设置
REQUESTS_TIME_OUT = (30, 30)

# 数据库 MySQL - 迁移
DB_MYSQL = {
    'host': HOST,
    'user': 'root',
    'passwd': '123456',
    'port': 3306,
    'db': 'lims_project'
}

SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqldb://%(user)s:%(passwd)s@%(host)s:%(port)s/%(db)s?charset=utf8mb4' % DB_MYSQL

SQLALCHEMY_BINDS = {
    'db_lims': SQLALCHEMY_DATABASE_URI
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_POOL_SIZE = 5  # 默认 pool_size=5
# SQLALCHEMY_MAX_OVERFLOW = 10  # 默认 10 连接池达到最大值后可以创建的连接数
# SQLALCHEMY_POOL_TIMEOUT = 10  # 默认 10秒
SQLALCHEMY_POOL_RECYCLE = 500  # 配置要小于 数据库配置 wait_timeout
SQLALCHEMY_ECHO = False

# 缓存，队列
REDIS = {
    'host': HOST,
    'port': 6379,
    # 'password': '123456'  # redis-cli AUTH 123456
}

REDIS_URL = 'redis://:%s@%s' % (REDIS['password'], REDIS['host']) \
    if REDIS.get('password') else 'redis://%s' % REDIS['host']

REDIS_PREFIX = 'lims'

SUCCESS_MSG = {
    'result': True,
    'message': '',
}

FAILURE_MSG = {
    'result': False,
    'message': '',
}

# Basic Auth
BASIC_AUTH_USERNAME = 'username'
BASIC_AUTH_PASSWORD = 'password'

# Endpoint
ENDPOINT = 'http://%s:%s' % (HOST, PORT)

# 页码默认配置
DEFAULT_PAGE = 1
DEFAULT_SITE = 20

if __name__ == '__main__':
    sk = os.urandom(24)
    print(sk)
    print(binascii.b2a_hex(sk))
