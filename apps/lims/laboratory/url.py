#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: url.py
@time: 2019-09-27 11:31
"""

from apps.lims.apis import api_lims
from apps.lims.laboratory.resource import (
    LaboratoryResource,
    LaboratoriesResource,
)

# 详情、修改、删除
api_lims.add_resource(
    LaboratoryResource,
    '/laboratory/<int:pk>',
    endpoint='laboratory',
    strict_slashes=False
)

# 创建、列表
api_lims.add_resource(
    LaboratoriesResource,
    '/laboratory',
    endpoint='laboratories',
    strict_slashes=False
)
