#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: request.py
@time: 2019-09-27 11:31
"""

from __future__ import unicode_literals

from flask_restful import reqparse

structure_key_item = 'contact'

request_parser = reqparse.RequestParser()
request_parser.add_argument(structure_key_item, type=dict, location='json')

request_parser_item = reqparse.RequestParser(trim=True, bundle_errors=True)

# POST
request_post = request_parser_item.copy()

request_post.add_argument(
    name='cid',
    location=structure_key_item,
    store_missing=False,
    required=True,
    help='单位必填',
)
request_post.add_argument(
    name='name',
    location=structure_key_item,
    store_missing=False,
    required=True,
    help='姓名必填',
)
request_post.add_argument(
    name='mobile',
    location=structure_key_item,
    store_missing=False,
)
request_post.add_argument(
    name='email',
    location=structure_key_item,
    store_missing=False,
)
request_post.add_argument(
    name='note',
    location=structure_key_item,
    store_missing=False,
)

# PUT
request_put = request_parser_item.copy()

request_put.add_argument(
    name='cid',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='name',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='mobile',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='email',
    location=structure_key_item,
    store_missing=False,
)
request_put.add_argument(
    name='note',
    location=structure_key_item,
    store_missing=False,
)

# DELETE
request_delete = request_parser_item.copy()

request_delete.add_argument(
    name='id',
    type=int,
    action='append',
    location=structure_key_item,
    store_missing=False,
    required=True,
    help='ID必填',
)
