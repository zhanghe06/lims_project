#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: url.py
@time: 2019-09-27 11:31
"""

from apps.lims.apis import api_lims
from apps.lims.specimen_item.resource import (
    SpecimenItemResource,
    SpecimenItemsResource,
    SpecimenCloneResource,
)

# 详情、修改、删除
api_lims.add_resource(
    SpecimenItemResource,
    '/specimen_item/<int:pk>',
    endpoint='specimen_item',
    strict_slashes=False
)

# 创建、列表
api_lims.add_resource(
    SpecimenItemsResource,
    '/specimen_item',
    endpoint='specimen_items',
    strict_slashes=False
)

# 克隆
api_lims.add_resource(
    SpecimenCloneResource,
    '/specimen_item/clone',
    endpoint='specimen_item_clone',
    strict_slashes=False
)
