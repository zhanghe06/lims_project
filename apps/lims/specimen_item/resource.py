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
from apps.lims.specimen_item.api import (
    get_specimen_item_row_by_id,
    delete_specimen_item,
    get_specimen_item_pagination,
    add_specimen_item,
    edit_specimen_item,
)
from apps.lims.detection.api import (
    get_detection_row_by_id,
    delete_detection,
    get_detection_pagination,
    add_detection,
    edit_detection,
    get_detection_rows,
)
from apps.lims.specimen_item.request import (
    structure_key_item,
    request_parser,
    request_post,
    request_put,
    request_delete,
    request_clone,
)
from apps.lims.specimen_item.response import fields_item
from apps.maps.status_delete import STATUS_DEL_OK, STATUS_DEL_NO

DEFAULT_PAGE = app.config['DEFAULT_PAGE']
DEFAULT_SITE = app.config['DEFAULT_SITE']

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class SpecimenItemResource(Resource):
    """
    SpecimenItemResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/specimen_item/1
        :param pk:
        :return:
        """
        data = get_specimen_item_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/specimen_item/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "specimen_item": {
                    "name": "specimen_item name put"
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
        data = get_specimen_item_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 更新数据
        request_data = request_item_args
        result = edit_specimen_item(pk, request_data)

        if not result:
            abort(NotFound.code, message='更新失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '更新成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/specimen_item/1 -X DELETE
        :param pk:
        :return:
        """
        # 是否存在
        data = get_specimen_item_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 删除数据
        result = delete_specimen_item(pk)

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)


class SpecimenItemsResource(Resource):
    """
    SpecimenItemsResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:8000/specimen_item
            curl http://0.0.0.0:8000/specimen_item?page=1&size=20
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=DEFAULT_PAGE, location='args')
        filter_parser.add_argument('size', type=int, default=DEFAULT_SITE, location='args')
        filter_parser.add_argument('applicant_id', type=int, store_missing=False, location='args')
        filter_parser_args = filter_parser.parse_args()

        if not filter_parser_args:
            abort(BadRequest.code, message='参数错误', status=False)

        pagination_obj = get_specimen_item_pagination(
            status_delete=STATUS_DEL_NO,
            **filter_parser_args
        )

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_item)
        result['total'] = pagination_obj.total
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:8000/specimen_item -H "Content-Type: application/json" -X POST -d '
            {
                "specimen_item": {
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
        result = add_specimen_item(request_data)

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
                "specimen_item": {
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
        result = delete_specimen_item(request_data['id'])

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)


class SpecimenCloneResource(Resource):
    """
    SpecimenCloneResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def post(self):
        """
        Example:
            curl http://0.0.0.0:8000/specimen_clone -H "Content-Type: application/json" -X POST -d '
            {
                "specimen_clone": {
                    "id": 1
                }
            }'
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_clone.parse_args(req=request_args)

        if not request_item_args:
            abort(BadRequest.code, message='参数错误', status=False)

        request_data = request_item_args
        # 克隆子样
        specimen_row = get_specimen_item_row_by_id(request_data['id'])
        if not specimen_row:
            abort(NotFound.code, message='没有记录', status=False)
        if specimen_row.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        specimen_data = specimen_row.to_dict()
        specimen_data.pop('id', 0)
        specimen_data.pop('note', '')
        specimen_data.pop('create_time', None)
        specimen_data.pop('update_time', None)
        result_specimen_item_id = add_specimen_item(specimen_data)
        if not result_specimen_item_id:
            abort(BadRequest.code, message='克隆子样失败', status=False)
        # 克隆分配
        detection_rows = get_detection_rows(**{
            'specimen_item_id': request_data['id'],
            'status_delete': STATUS_DEL_NO,
        })
        for detection_row in detection_rows:
            detection_data = detection_row.to_dict()
            detection_data.pop('id', 0)
            detection_data.pop('create_time', None)
            detection_data.pop('update_time', None)
            detection_data['specimen_item_id'] = result_specimen_item_id
            result = add_detection(detection_data)
            if not result:
                abort(BadRequest.code, message='克隆分配失败', status=False)
        success_msg = SUCCESS_MSG.copy()
        success_msg['id'] = result_specimen_item_id
        success_msg['message'] = '克隆成功'
        return make_response(jsonify(success_msg), 200)
