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
    'salutation': fields.String(attribute='salutation'),
    'mobile': fields.String(attribute='mobile'),
    'tel': fields.String(attribute='tel'),
    'fax': fields.String(attribute='fax'),
    'email': fields.String(attribute='email'),
    'lab_id': fields.Integer(attribute='lab_id'),
    'dep_id': fields.Integer(attribute='dep_id'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
