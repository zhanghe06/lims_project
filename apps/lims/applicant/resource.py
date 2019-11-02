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
from apps.lims.applicant.api import (
    get_applicant_row_by_id,
    delete_applicant,
    get_applicant_pagination,
    add_applicant,
    edit_applicant,
)
from apps.lims.applicant.request import (
    structure_key_item,
    request_parser,
    request_post,
    request_put,
    request_delete,
)
from apps.models.model_lims import ReportInfo as Applicant
from apps.lims.applicant.response import fields_item
from apps.maps.status_delete import STATUS_DEL_OK, STATUS_DEL_NO

DEFAULT_PAGE = app.config['DEFAULT_PAGE']
DEFAULT_SITE = app.config['DEFAULT_SITE']

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class ApplicantResource(Resource):
    """
    ApplicantResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/applicant/1
        :param pk:
        :return:
        """
        data = get_applicant_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/applicant/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "applicant": {
                    "name": "applicant name put"
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
        data = get_applicant_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 更新数据
        request_data = request_item_args
        result = edit_applicant(pk, request_data)

        if not result:
            abort(NotFound.code, message='更新失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '更新成功'
        return make_response(jsonify(success_msg), 200)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/applicant/1 -X DELETE
        :param pk:
        :return:
        """
        # 是否存在
        data = get_applicant_row_by_id(pk)

        if not data:
            abort(NotFound.code, message='没有记录', status=False)
        if data.status_delete == STATUS_DEL_OK:
            abort(NotFound.code, message='已经删除', status=False)

        # 删除数据
        result = delete_applicant(pk)

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)


class ApplicantsResource(Resource):
    """
    ApplicantsResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:8000/applicant
            curl http://0.0.0.0:8000/applicant?page=1&size=20
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=DEFAULT_PAGE, location='args')
        filter_parser.add_argument('size', type=int, default=DEFAULT_SITE, location='args')
        filter_parser.add_argument('code', dest='report_no', store_missing=False, location='args')
        filter_parser_args = filter_parser.parse_args()

        if not filter_parser_args:
            abort(BadRequest.code, message='参数错误', status=False)

        filter_args = []
        code = filter_parser_args.pop('code', '')
        if code:
            filter_args.append(Applicant.report_no.like('%%%s%%' % code))

        filter_parser_args['status_delete'] = STATUS_DEL_NO
        pagination_obj = get_applicant_pagination(
            filter_parser_args.pop('page'),
            filter_parser_args.pop('size'),
            *filter_args,
            **filter_parser_args
        )

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_item)
        result['total'] = pagination_obj.total
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:8000/applicant -H "Content-Type: application/json" -X POST -d '
            {
                "applicant": {
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
        result = add_applicant(request_data)

        if not result:
            abort(BadRequest.code, message='创建失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['id'] = result
        success_msg['message'] = '创建成功'
        # fixme
        year_code = '2019'
        dep_code = 'FZ01'
        index_code = '%06d' % (result % 1000000)
        code = 'NZJ(%s)%s-%s' % (year_code, dep_code, index_code)
        edit_applicant(result, {'code': code})
        return make_response(jsonify(success_msg), 200)

    def delete(self):
        """
        Example:
            curl http://0.0.0.0:8000/user -X DELETE -d '
            {
                "applicant": {
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
        result = delete_applicant(request_data['id'])

        if not result:
            abort(BadRequest.code, message='删除失败', status=False)

        success_msg = SUCCESS_MSG.copy()
        success_msg['message'] = '删除成功'
        return make_response(jsonify(success_msg), 200)
