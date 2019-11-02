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
    'code': fields.String(attribute='report_no'),
    'receiver_uid': fields.Integer(attribute='receiver_uid'),
    'applicant_cid': fields.Integer(attribute='submitter_cid'),
    'applicant_uid': fields.Integer(attribute='submitter_uid'),
    'detection_cid': fields.Integer(attribute='be_inspected_entity_cid'),
    'type_detection': fields.Integer(attribute='inspection_type'),
    'type_test': fields.Integer(attribute='test_type'),
    'grade_id': fields.Integer(attribute='sample_grade_id'),
    'summary': fields.String(attribute='sample_quantity'),
    'note': fields.String(attribute='sample_description'),
    'style': fields.String(attribute='style_number'),
    'sku': fields.String(attribute='sku_number'),
    'brand': fields.String(attribute='sample_brand'),
    'period': fields.Integer(attribute='period'),
    'req_date': fields.DateTime(dt_format=b'iso8601'),
    'arr_date': fields.DateTime(dt_format=b'iso8601'),
    'create_time': fields.DateTime(dt_format=b'iso8601'),
    'update_time': fields.DateTime(dt_format=b'iso8601'),
}
