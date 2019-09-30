#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: url.py
@time: 2019-09-27 11:31
"""

from apps.lims.apis import api_lims
from apps.lims.company.resource import (
    CompanyResource,
    CompaniesResource,
)

# 客户详情（详情、修改、删除）
api_lims.add_resource(
    CompanyResource,
    '/company/<int:pk>',
    endpoint='company',
    strict_slashes=False
)

# 客户列表（创建、列表）
api_lims.add_resource(
    CompaniesResource,
    '/company',
    endpoint='companies',
    strict_slashes=False
)
