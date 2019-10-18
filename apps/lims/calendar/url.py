#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: url.py
@time: 2019-09-27 11:31
"""

from apps.lims.apis import api_lims
from apps.lims.calendar.resource import (
    CalendarResource,
    CalendarsResource,
    CalendarDateDeltaResource,
)

# 详情、修改、删除
api_lims.add_resource(
    CalendarResource,
    '/calendar/<int:pk>',
    endpoint='calendar',
    strict_slashes=False
)

# 创建、列表
api_lims.add_resource(
    CalendarsResource,
    '/calendar',
    endpoint='calendars',
    strict_slashes=False
)

# 日期
api_lims.add_resource(
    CalendarDateDeltaResource,
    '/calendar/date/delta',
    endpoint='calendar_date_delta',
    strict_slashes=False
)
