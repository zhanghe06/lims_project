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
    'receiver_uid': fields.Integer(attribute='receiver_uid'),
    'applicant_cid': fields.Integer(attribute='applicant_cid'),
    'applicant_uid': fields.Integer(attribute='applicant_uid'),
    'detection_cid': fields.Integer(attribute='detection_cid'),
    'type_detection': fields.Integer(attribute='type_detection'),
    'type_test': fields.Integer(attribute='type_test'),
    'grade_id': fields.Integer(attribute='grade_id'),
    'summary': fields.String(attribute='summary'),
    'note': fields.String(attribute='note'),
    'style': fields.String(attribute='style'),
    'sku': fields.String(attribute='sku'),
    'brand': fields.String(attribute='brand'),
    'period': fields.Integer(attribute='period'),
    'req_date': fields.DateTime(dt_format=b'iso8601'),
    'arr_date': fields.DateTime(dt_format=b'iso8601'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
