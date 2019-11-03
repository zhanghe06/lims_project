#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: resource.py
@time: 2019-09-27 11:32
"""

from __future__ import unicode_literals

import datetime
from flask import jsonify, make_response
from flask_restful import Resource, marshal, reqparse, abort
from werkzeug.exceptions import NotFound, BadRequest

from apps import app
from apps.lims.detection.api import (
    get_detection_row_by_id,
    delete_detection,
    get_detection_pagination,
    add_detection,
    edit_detection,
    get_detection_rows,
)
from apps.lims.specimen_item.api import (
    get_specimen_item_row_by_id,
    delete_specimen_item,
    get_specimen_item_pagination,
    add_specimen_item,
    edit_specimen_item,
)
from apps.lims.detection.request import (
    structure_key_item,
    request_parser,
    request_post,
    request_put,
    request_delete,
)
from apps.lims.detection.response import fields_item
from apps.maps.status_delete import STATUS_DEL_OK, STATUS_DEL_NO

DEFAULT_PAGE = app.config['DEFAULT_PAGE']
DEFAULT_SITE = app.config['DEFAULT_SITE']

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class DetectionResource(Resource):
    """
    DetectionResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/detection/1
        :param pk:
        :return:
        """
        data = get_detection_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/detection/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "detection": {
                    "name": "detection name put"
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
        data = get_detection_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 更新数据
        request_data = request_item_args
        result = edit_detection(pk, request_data)

        if not result:
            abort(NotFound.code, message='更新失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '更新成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/detection/1 -X DELETE
        :param pk:
        :return:
        """
        # 是否存在
        data = get_detection_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 删除数据
        result = delete_detection(pk)

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)


class DetectionsResource(Resource):
    """
    DetectionsResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:8000/detection
            curl http://0.0.0.0:8000/detection?page=1&size=20
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=DEFAULT_PAGE, location='args')
        filter_parser.add_argument('size', type=int, default=DEFAULT_SITE, location='args')
        filter_parser.add_argument('specimen_item_id', dest='sub_sample_id', type=int, store_missing=False, location='args')
        filter_parser_args = filter_parser.parse_args()

        if not filter_parser_args:
            abort(BadRequest.code, message='参数错误', status=False)

        pagination_obj = get_detection_pagination(
            status_delete=STATUS_DEL_NO,
            **filter_parser_args
        )

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_item)
        result['total'] = pagination_obj.total
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:8000/detection -H "Content-Type: application/json" -X POST -d '
            {
                "detection": {
                    "name": "a",
                    "specimen_item_id": 1,
                    "manner_id": 1,
                    "note": "hello"
                }
            }'
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_post.parse_args(req=request_args)

        if not request_item_args:
            abort(BadRequest.code, message='参数错误', status=False)

        request_data = request_item_args

        manner_ids = request_data.pop('test_method_id', [])  # 关联数据
        for manner_id in manner_ids:
            request_data['test_method_id'] = manner_id
            result = add_detection(request_data)

            if not result:
                abort(BadRequest.code, message='创建失败', status=False)

        # 更新子样分配状态
        if manner_ids:
            edit_specimen_item(
                request_item_args['sub_sample_id'],
                {'status_allocate': 1}
            )
        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '创建成功'
        return make_response(jsonify(success_msg), 200)

    def put(self):
        """
        根据子样编号修改数据
        Example:
            curl http://0.0.0.0:8000/detection -H "Content-Type: application/json" -X PUT -d '
            {
                "detection": {
                    "specimen_item_id": 5,
                    "manner_id": [1],
                    "note": "hello"
                }
            }'
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_put.parse_args(req=request_args)

        if not request_item_args:
            abort(BadRequest.code, message='参数错误', status=False)

        # 是否存在(子样ID，并非分配ID)
        data = get_specimen_item_row_by_id(request_item_args['sub_sample_id'])

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 更新数据
        request_data = request_item_args
        manner_ids = request_data.pop('test_method_id', [])  # 关联数据
        # 关联数据（2步）
        result = False
        # 1. 清除历史
        detection_rows = get_detection_rows(
            **{
                'sub_sample_id': request_data['sub_sample_id'],
                'status_delete': STATUS_DEL_NO,
            }
        )
        detection_ids = [detection_row.id for detection_row in detection_rows]
        if detection_ids:
            result = delete_detection(detection_ids)
            if not result:
                abort(BadRequest.code, message='删除失败', status=False)
        # 2. 新增更新
        for manner_id in manner_ids:
            request_data['test_method_id'] = manner_id
            result = add_detection(request_data)

            if not result:
                abort(BadRequest.code, message='创建失败', status=False)

        if not result:
            abort(NotFound.code, message='更新失败', status=False)

        # 更新子样分配状态
        if manner_ids:
            status_allocate = 1
            allocate_time = datetime.datetime.now()
        else:
            status_allocate = 0
            allocate_time = None
        edit_specimen_item(
            request_item_args['sub_sample_id'],
            {
                'status_allocate': status_allocate,
                'allocate_time': allocate_time,
            }
        )

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '更新成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self):
        """
        Example:
            curl http://0.0.0.0:8000/user -X DELETE -d '
            {
                "detection": {
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
        detection_ids = request_data['id']

        detection_row = get_detection_row_by_id(detection_ids[0])
        if not detection_row:
            abort(NotFound.code, message='没有记录', status=False)
        sub_sample_id = detection_row.sub_sample_id

        result = delete_detection(detection_ids)

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        # 更新子样分配状态 todo
        detection_rows = get_detection_rows(**{
            'sub_sample_id': sub_sample_id,
            'status_delete': STATUS_DEL_NO,
        })
        if detection_rows:
            status_allocate = 1
            allocate_time = datetime.datetime.now()
        else:
            status_allocate = 0
            allocate_time = None
        edit_specimen_item(
            sub_sample_id,
            {
                'status_allocate': status_allocate,
                'allocate_time': allocate_time,
            }
        )

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)
