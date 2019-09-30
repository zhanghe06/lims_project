#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: request.py
@time: 2019-09-27 11:31
"""

from __future__ import unicode_literals

from flask_restful import reqparse, inputs

structure_key_item = 'company'

request_parser = reqparse.RequestParser()
request_parser.add_argument(structure_key_item, type=dict, location='json')

request_parser_item = reqparse.RequestParser(trim=True, bundle_errors=True)

# POST
request_post = request_parser_item.copy()

request_post.add_argument(
    name='name',
    location=structure_key_item,
    store_missing=False,
    required=True,
    help='公司名称必填',
)
request_post.add_argument(
    name='address',
    location=structure_key_item,
    store_missing=False,
    required=False,
)
request_post.add_argument(
    name='site',
    location=structure_key_item,
    store_missing=False,
)
request_post.add_argument(
    name='tel',
    location=structure_key_item,
    store_missing=False,
)
request_post.add_argument(
    name='fax',
    location=structure_key_item,
    store_missing=False,
)
request_post.add_argument(
    name='type',
    type=inputs.int_range(0, 2),
    location=structure_key_item,
    store_missing=False,
    required=True,
    help='公司类型必填',
)

# PUT
request_put = request_parser_item.copy()

request_put.add_argument(
    name='name',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='address',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='site',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='tel',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='fax',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='type',
    type=inputs.int_range(0, 2),
    location=structure_key_item,
    store_missing=False,
)
