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
from werkzeug.exceptions import NotFound, BadRequest

from apps import app
from apps.lims.standard.api import (
    get_standard_row_by_id,
    delete_standard,
    get_standard_pagination,
    add_standard,
    edit_standard,
)
from apps.lims.map_standard_manner.api import (
    add_map_standard_manner,
    get_map_standard_manner_rows,
    delete_map_standard_manner,
)
from apps.lims.standard.request import (
    structure_key_item,
    request_parser,
    request_post,
    request_put,
    request_delete,
)
from apps.lims.standard.response import fields_item
from apps.maps.status_delete import STATUS_DEL_OK, STATUS_DEL_NO
from apps.models.model_lims import MapStandardManner

DEFAULT_PAGE = app.config['DEFAULT_PAGE']
DEFAULT_SITE = app.config['DEFAULT_SITE']

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class StandardResource(Resource):
    """
    StandardResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/standard/1
        :param pk:
        :return:
        """
        data = get_standard_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/standard/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "standard": {
                    "name": "standard name put"
                }
            }'
        :param pk:
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_put.parse_args(req=request_args)

        if not request_item_args:
            abort(BadRequest.code, message='参数错误', status=False)

        # 是否存在
        data = get_standard_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 更新数据
        request_data = request_item_args
        manner_ids = request_item_args.pop('manner_id', [])  # 关联数据
        # 关联数据（2步）
        # 1. 清除历史
        map_rows = get_map_standard_manner_rows(**{'standard_id': pk})
        map_ids = [map_row.id for map_row in map_rows]
        if map_ids:
            result = delete_map_standard_manner(map_ids)
            if not result:
                abort(BadRequest.code, message='删除失败', status=False)
        # 2. 新增更新
        for manner_id in manner_ids:
            map_data = {
                'standard_id': pk,
                'manner_id': manner_id,
            }
            result = add_map_standard_manner(map_data)
            if not result:
                abort(BadRequest.code, message='创建失败', status=False)
        result = edit_standard(pk, request_data)

        if not result:
            abort(NotFound.code, message='更新失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '更新成功'
        return make_response(jsonify(success_msg), 200)

    # def delete(self, pk):
    #     """
    #     Example:
    #         curl http://0.0.0.0:8000/standard/1 -X DELETE
    #     :param pk:
    #     :return:
    #     """
    #     # 是否存在
    #     data = get_standard_row_by_id(pk)
    #
    #     if not data:
    #         abort(NotFound.code, message='没有记录', status=False)
    #     if data.status_delete == STATUS_DEL_OK:
    #         abort(NotFound.code, message='已经删除', status=False)
    #
    #     # 删除数据
    #     result = delete_standard(pk)
    #
    #     if not result:
    #         abort(BadRequest.code, message='删除失败', status=False)
    #
    #     success_msg = SUCCESS_MSG.copy()
    #     success_msg['message'] = '删除成功'
    #     return make_response(jsonify(success_msg), 200)


class StandardsResource(Resource):
    """
    StandardsResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:8000/standard
            curl http://0.0.0.0:8000/standard?page=1&size=20
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=DEFAULT_PAGE, location='args')
        filter_parser.add_argument('size', type=int, default=DEFAULT_SITE, location='args')
        filter_parser_args = filter_parser.parse_args()

        if not filter_parser_args:
            abort(BadRequest.code, message='参数错误', status=False)

        pagination_obj = get_standard_pagination(
            status_delete=STATUS_DEL_NO,
            **filter_parser_args
        )

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_item)
        result['total'] = pagination_obj.total
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:8000/standard -H "Content-Type: application/json" -X POST -d '
            {
                "standard": {
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

        request_data = request_item_args
        manner_ids = request_item_args.pop('manner_id', [])  # 关联数据
        result = add_standard(request_data)

        if not result:
            abort(BadRequest.code, message='创建失败', status=False)
        # 关联数据
        for manner_id in manner_ids:
            map_data = {
                'standard_id': result,
                'manner_id': manner_id,
            }
            result = add_map_standard_manner(map_data)
            if not result:
                abort(BadRequest.code, message='创建失败', status=False)
        success_msg = SUCCESS_MSG.copy()
        success_msg['id'] = result
        success_msg['message'] = '创建成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self):
        """
        Example:
            curl http://0.0.0.0:8000/user -X DELETE -d '
            {
                "standard": {
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
        result = delete_standard(request_data['id'])

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)
