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
    'applicant_id': fields.Integer(attribute='applicant_id'),
    'grade_id': fields.Integer(attribute='grade_id'),
    'style': fields.String(attribute='style'),
    'sku': fields.String(attribute='sku'),
    'brand': fields.String(attribute='brand'),
    'period': fields.Integer(attribute='period'),
    'req_date': fields.DateTime(dt_format=b'iso8601'),
    'note': fields.String(attribute='note'),
    'arr_date': fields.DateTime(dt_format=b'iso8601'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
