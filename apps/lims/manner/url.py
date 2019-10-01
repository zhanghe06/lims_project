#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: url.py
@time: 2019-09-27 11:31
"""

from apps.lims.apis import api_lims
from apps.lims.manner.resource import (
    MannerResource,
    MannersResource,
)

# 详情、修改、删除
api_lims.add_resource(
    MannerResource,
    '/manner/<int:pk>',
    endpoint='manner',
    strict_slashes=False
)

# 创建、列表
api_lims.add_resource(
    MannersResource,
    '/manner',
    endpoint='manners',
    strict_slashes=False
)
