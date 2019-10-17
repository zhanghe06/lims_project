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
    'code': fields.String(attribute='code'),
    'name': fields.String(attribute='name'),
    # 'specimen_id': fields.Integer(attribute='specimen_id'),  # TODO 废弃
    'note': fields.String(attribute='note'),
    'status_allocate': fields.Integer(attribute='status_allocate'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
