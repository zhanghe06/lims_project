#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: resource.py
@time: 2019-09-27 11:32
"""

from __future__ import unicode_literals

from flask import jsonify, make_response
from flask_restful import Resource, marshal, reqparse, abort
from sqlalchemy import or_
from werkzeug.exceptions import NotFound, BadRequest

from apps import app
from apps.lims.analyze.api import (
    delete_analyze,
    add_analyze,
    get_analyze_rows,
)
from apps.lims.manner.api import (
    get_manner_row_by_id,
    delete_manner,
    get_manner_pagination,
    add_manner,
    edit_manner,
)
from apps.lims.manner.request import (
    structure_key_item,
    request_parser,
    request_post,
    request_put,
    request_delete,
)
from apps.lims.manner.response import fields_item
from apps.lims.map_standard_manner.api import (
    get_map_standard_manner_rows,
)
from apps.maps.status_delete import STATUS_DEL_OK, STATUS_DEL_NO
from apps.models.model_lims import TestMethod as Manner

DEFAULT_PAGE = app.config['DEFAULT_PAGE']
DEFAULT_SITE = app.config['DEFAULT_SITE']

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class MannerResource(Resource):
    """
    MannerResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/manner/1
        :param pk:
        :return:
        """
        data = get_manner_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/manner/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "manner": {
                    "name": "manner name put"
                }
            }'
        :param pk:
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_put.parse_args(req=request_args)

        if not request_item_args:
            abort(BadRequest.code, message='参数错误', status=False)
        analyze_list_args = request_item_args.pop('analyze', [])
        for analyze_item_args in analyze_list_args:
            if {'property', 'sort_code'} != set(analyze_item_args.keys()):
                abort(BadRequest.code, message='参数错误', status=False)

        # 是否存在
        data = get_manner_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 更新数据
        request_data = request_item_args
        result = edit_manner(pk, request_data)

        if not result:
            abort(NotFound.code, message='更新失败', status=False)

        # 1. 清除历史
        analyze_rows = get_analyze_rows(**{'test_method_id': pk, 'status_delete': STATUS_DEL_NO})
        analyze_ids = [analyze_row.id for analyze_row in analyze_rows]
        if analyze_ids:
            result = delete_analyze(analyze_ids)
            if not result:
                abort(BadRequest.code, message='删除失败', status=False)
        # 2. 新增更新
        for analyze_data in analyze_list_args:
            analyze_data['test_method_id'] = pk
            result_analyze_id = add_analyze(analyze_data)
            if not result_analyze_id:
                abort(BadRequest.code, message='创建失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '更新成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/manner/1 -X DELETE
        :param pk:
        :return:
        """
        # 是否存在
        data = get_manner_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 删除数据
        result = delete_manner(pk)

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)


class MannersResource(Resource):
    """
    MannersResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:8000/manner
            curl http://0.0.0.0:8000/manner?page=1&size=20
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=DEFAULT_PAGE, location='args')
        filter_parser.add_argument('size', type=int, default=DEFAULT_SITE, location='args')
        filter_parser.add_argument('standard_id', dest='protocol_id', type=int, store_missing=False, location='args')
        filter_parser.add_argument('keywords', store_missing=False, location='args')
        filter_parser_args = filter_parser.parse_args()

        if not filter_parser_args:
            abort(BadRequest.code, message='参数错误', status=False)

        filter_args = []
        # 模糊搜索
        keywords = filter_parser_args.pop('keywords', '')
        if keywords:
            filter_args.append(or_(Manner.code.like('%%%s%%' % keywords), Manner.name.like('%%%s%%' % keywords)))

        standard_id = filter_parser_args.pop('protocol_id', 0)
        # 获取关联数据
        if standard_id:
            map_rows = get_map_standard_manner_rows(**{'protocol_id': standard_id, 'status_delete': STATUS_DEL_NO})
            manner_ids = [map_row.test_method_id for map_row in map_rows]
            filter_args.append(Manner.id.in_(manner_ids))

        filter_parser_args['status_delete'] = STATUS_DEL_NO
        pagination_obj = get_manner_pagination(
            filter_parser_args.pop('page'),
            filter_parser_args.pop('size'),
            *filter_args,
            **filter_parser_args
        )

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_item)
        for i in result[structure_key_item]:
            i['standard_id'] = standard_id
        result['total'] = pagination_obj.total
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:8000/manner -H "Content-Type: application/json" -X POST -d '
            {
                "manner": {
                    "name": "tom",
                    "salutation": "先生",
                    "mobile": "http://www.baidu.com",
                    "tel": "021-62345678",
                    "fax": "021-62345678",
                    "email": "haha@haha.com"
                }
            }'
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_post.parse_args(req=request_args)

        if not request_item_args:
            abort(BadRequest.code, message='参数错误', status=False)
        analyze_list_args = request_item_args.pop('analyze', [])
        for analyze_item_args in analyze_list_args:
            if {'property', 'sort_code'} != set(analyze_item_args.keys()):
                abort(BadRequest.code, message='参数错误', status=False)

        request_data = request_item_args
        result_manner_id = add_manner(request_data)

        if not result_manner_id:
            abort(BadRequest.code, message='创建失败', status=False)

        for analyze_data in analyze_list_args:
            analyze_data['test_method_id'] = result_manner_id
            result_analyze_id = add_analyze(analyze_data)
            if not result_analyze_id:
                abort(BadRequest.code, message='创建失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['id'] = result_manner_id
        success_msg['message'] = '创建成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self):
        """
        Example:
            curl http://0.0.0.0:8000/user -X DELETE -d '
            {
                "manner": {
                    "id": [1, 2]
                }
            }'
        :return:
        """
        # 是否存在
        request_args = request_parser.parse_args()
        request_item_args = request_delete.parse_args(req=request_args)

        if not request_item_args:
            abort(BadRequest.code, message='参数错误', status=False)

        request_data = request_item_args
        result = delete_manner(request_data['id'])

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)
