#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: response.py
@time: 2019-09-27 11:30
"""

from __future__ import unicode_literals

from flask_restful import fields

fields_item = {
    'id': fields.Integer(attribute='id'),
    'name': fields.String(attribute='name'),
    'date': fields.String(attribute='date'),
    'week': fields.Integer(attribute='week'),
    'status_holiday': fields.Boolean(attribute='status_holiday'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
