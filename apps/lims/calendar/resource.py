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
import datetime
from libs.calendar_days import get_delta_date, get_week
from apps import app
from apps.lims.calendar.api import (
    get_calendar_row_by_id,
    delete_calendar,
    get_calendar_pagination,
    add_calendar,
    edit_calendar,
    get_calendar_rows,
)
from apps.lims.calendar.request import (
    structure_key_item,
    request_parser,
    request_post,
    request_put,
    request_delete,
)
from apps.lims.calendar.response import fields_item
from apps.maps.status_delete import STATUS_DEL_OK, STATUS_DEL_NO

DEFAULT_PAGE = app.config['DEFAULT_PAGE']
DEFAULT_SITE = app.config['DEFAULT_SITE']

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class CalendarResource(Resource):
    """
    CalendarResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/calendar/1
        :param pk:
        :return:
        """
        data = get_calendar_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/calendar/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "calendar": {
                    "name": "周六出去玩",
                    "date": "2019-10-19",
                    "status_holiday": true
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
        data = get_calendar_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 更新数据
        request_data = request_item_args
        request_data['week'] = get_week(request_data['date'])
        result = edit_calendar(pk, request_data)

        if not result:
            abort(NotFound.code, message='更新失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '更新成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/calendar/1 -X DELETE
        :param pk:
        :return:
        """
        # 是否存在
        data = get_calendar_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 删除数据
        result = delete_calendar(pk)

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)


class CalendarsResource(Resource):
    """
    CalendarsResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:8000/calendar
            curl http://0.0.0.0:8000/calendar?page=1&size=20
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=DEFAULT_PAGE, location='args')
        filter_parser.add_argument('size', type=int, default=DEFAULT_SITE, location='args')
        filter_parser_args = filter_parser.parse_args()

        if not filter_parser_args:
            abort(BadRequest.code, message='参数错误', status=False)

        pagination_obj = get_calendar_pagination(
            status_delete=STATUS_DEL_NO,
            **filter_parser_args
        )

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_item)
        result['total'] = pagination_obj.total
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:8000/calendar -H "Content-Type: application/json" -X POST -d '
            {
                "calendar": {
                    "name": "周六",
                    "date": "2019-10-19",
                    "status_holiday": true
                }
            }'
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_post.parse_args(req=request_args)

        if not request_item_args:
            abort(BadRequest.code, message='参数错误', status=False)

        request_data = request_item_args
        request_data['week'] = get_week(request_data['date'])
        result = add_calendar(request_data)

        if not result:
            abort(BadRequest.code, message='创建失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['id'] = result
        success_msg['message'] = '创建成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self):
        """
        Example:
            curl http://0.0.0.0:8000/calendar -X DELETE -d '
            {
                "calendar": {
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
        result = delete_calendar(request_data['id'])

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)


class CalendarDateDeltaResource(Resource):
    """
    CalendarDateDeltaResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:8000/calendar/date/delta
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('current_day', location='args')
        filter_parser.add_argument('delta_day', type=int, default=1, location='args')
        filter_parser_args = filter_parser.parse_args()

        if not filter_parser_args:
            abort(BadRequest.code, message='参数错误', status=False)

        # 默认当天
        if not filter_parser_args['current_day']:
            filter_parser_args['current_day'] = datetime.datetime.now().date().strftime('%Y-%m-%d')

        # todo
        holiday_rows = get_calendar_rows(**{
            'status_holiday': 1,
            'status_delete': 0,
        })
        holiday_days = [holiday_row.date.strftime('%Y-%m-%d') for holiday_row in holiday_rows]
        date_delta = get_delta_date(
            filter_parser_args['delta_day'],
            filter_parser_args['current_day'],
            True,
            holiday_days,
        )

        success_msg = SUCCESS_MSG.copy()
        success_msg['date'] = date_delta
        success_msg['message'] = '获取成功'
        return make_response(jsonify(success_msg), 200)
