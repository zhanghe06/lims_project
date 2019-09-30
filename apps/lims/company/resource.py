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
from flask_restful import Resource, marshal, reqparse

from apps import app
from apps.commons.exceptions import NotFound, BadRequest
from apps.lims.company.api import (
    get_company_row_by_id,
    delete_company,
    get_company_pagination,
    add_company,
    edit_company,
)
from apps.lims.company.request import (
    structure_key_item,
    request_parser,
    request_post,
    request_put,
)
from apps.lims.company.response import fields_item
from apps.maps.status_delete import STATUS_DEL_NO

DEFAULT_PAGE = app.config['DEFAULT_PAGE']
DEFAULT_SITE = app.config['DEFAULT_SITE']

SUCCESS_MSG = app.config['SUCCESS_MSG']
FAILURE_MSG = app.config['FAILURE_MSG']


class CompanyResource(Resource):
    """
    CompanyResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/company/1
        :param pk:
        :return:
        """
        data = get_company_row_by_id(pk)
        if not data:
            raise NotFound
        result = marshal(data, fields_item, envelope=structure_key_item)
        return jsonify(result)

    def put(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/company/1 -H "Content-Type: application/json" -X PUT -d '
            {
                "company": {
                    "name": "company name put"
                }
            }'
        :param pk:
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_put.parse_args(req=request_args)
        if not request_item_args:
            raise BadRequest

        request_data = request_item_args
        result = edit_company(pk, request_data)
        if result:
            success_msg = SUCCESS_MSG.copy()
            success_msg['message'] = '更新成功'
            return make_response(jsonify(success_msg), 200)
        else:
            failure_msg = FAILURE_MSG.copy()
            failure_msg['message'] = '更新失败'
            return make_response(jsonify(failure_msg), 400)

    def delete(self, pk):
        """
        Example:
            curl http://0.0.0.0:8000/company/1 -X DELETE
        :param pk:
        :return:
        """
        result = delete_company(pk)
        if result:
            success_msg = SUCCESS_MSG.copy()
            success_msg['message'] = '删除成功'
            return make_response(jsonify(success_msg), 200)
        else:
            failure_msg = FAILURE_MSG.copy()
            failure_msg['message'] = '删除失败'
            return make_response(jsonify(failure_msg), 400)


class CompaniesResource(Resource):
    """
    CompaniesResource
    """
    decorators = [
        # token_auth.login_required,
    ]

    def get(self):
        """
        Example:
            curl http://0.0.0.0:8000/company
            curl http://0.0.0.0:8000/company?page=1&size=20
        :return:
        """
        # 条件参数
        filter_parser = reqparse.RequestParser(bundle_errors=True)
        filter_parser.add_argument('page', type=int, default=DEFAULT_PAGE, location='args')
        filter_parser.add_argument('size', type=int, default=DEFAULT_SITE, location='args')

        filter_parser_args = filter_parser.parse_args()

        pagination_obj = get_company_pagination(
            status_delete=STATUS_DEL_NO,
            **filter_parser_args
        )

        result = marshal(pagination_obj.items, fields_item, envelope=structure_key_item)
        result['total'] = pagination_obj.total
        return jsonify(result)

    def post(self):
        """
        Example:
            curl http://0.0.0.0:8000/company -H "Content-Type: application/json" -X POST -d '
            {
                "company": {
                    "name": "company name",
                    "address": "company address",
                    "site": "http://www.baidu.com",
                    "tel": "021-62345678",
                    "fax": "021-62345678",
                    "type": 1
                }
            }'
        :return:
        """
        request_args = request_parser.parse_args()
        request_item_args = request_post.parse_args(req=request_args)
        if not request_item_args:
            raise BadRequest

        request_data = request_item_args
        result = add_company(request_data)
        if result:
            success_msg = SUCCESS_MSG.copy()
            success_msg['id'] = result
            success_msg['message'] = '创建成功'
            return make_response(jsonify(success_msg), 200)
        raise NotFound
