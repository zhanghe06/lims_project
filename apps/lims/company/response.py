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
    'id': fields.String(attribute='id'),
    'name': fields.String(attribute='name'),
    'address': fields.String(attribute='address'),
    'site': fields.String(attribute='site'),
    'tel': fields.String(attribute='tel'),
    'fax': fields.String(attribute='fax'),
    'email': fields.String(attribute='email'),
    'type': fields.Integer(attribute='type'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
