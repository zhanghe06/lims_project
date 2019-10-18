#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: calendar_days.py
@time: 2019-10-18 16:51
"""


import json
import calendar
import datetime


def __default(obj):
    """
    支持datetime的json encode
    TypeError: datetime.datetime(2015, 10, 21, 8, 42, 54) is not JSON serializable
    :param obj:
    :return:
    """
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)


def get_week(day=None):
    """获取星期"""
    if not day:
        return datetime.datetime.now().weekday() + 1
    return datetime.datetime.strptime(day, '%Y-%m-%d').weekday() + 1


def delta_date(day, delta_day=1):
    """变更日期"""
    nex_day_obj = datetime.datetime.strptime(day, '%Y-%m-%d') + datetime.timedelta(days=delta_day)
    return nex_day_obj.strftime('%Y-%m-%d')


def union_days(days_main, days_other):
    """并集"""
    days = list(set(days_main) | set(days_other))
    days.sort()
    return days


def difference_days(days_main, days_other):
    """差集"""
    days = list(set(days_main) - set(days_other))
    days.sort()
    return days


def get_year_days(year=None):
    # 默认当年
    if year is None:
        year = datetime.datetime.now().year

    # 年，季，月，周
    year_days = calendar.Calendar().yeardatescalendar(year)

    days_calendar = []
    for quarter_days in year_days:
        for month_days in quarter_days:
            for week_days in month_days:
                days_calendar.extend(week_days)
    days = list(set(json.loads(json.dumps(days_calendar, default=__default))))
    days.sort()
    return days


def get_holiday_days(year=None):
    """假期（这里假定周末）"""
    # 默认当年
    if year is None:
        year = datetime.datetime.now().year

    # 年，季，月，周
    year_days = calendar.Calendar().yeardatescalendar(year)

    holiday_days = []
    for quarter_days in year_days:
        for month_days in quarter_days:
            for week_days in month_days:
                holiday_days.extend(week_days[5:])
    days = list(set(json.loads(json.dumps(holiday_days, default=__default))))
    days.sort()
    return days


def get_delta_date(delta_day=1, start_day=None, skip_holiday=False, holiday_days=None):
    """
    get_delta_date(10, '2018-11-24') -> '2018-12-04'
    get_delta_date(10, '2019-11-24') -> '2019-12-04'
    get_delta_date(20, '2019-12-24') -> '2020-01-13'
    get_delta_date(396, '2019-12-24') -> '2021-01-23'
    :param delta_day:
    :param start_day:
    :param skip_holiday:
    :param holiday_days:
    :return:
    """
    if not start_day:
        # 默认 当天、当年
        start_day = datetime.datetime.now().date().strftime('%Y-%m-%d')
        year = datetime.datetime.now().year
    else:
        # 指定 年份
        year = datetime.datetime.strptime(start_day, '%Y-%m-%d').year

    year_days = get_year_days(year)
    if skip_holiday:
        holiday_days = holiday_days or get_holiday_days(year)
        year_days = difference_days(year_days, holiday_days)
    while 1:
        try:
            start_day_index = year_days.index(start_day)
            break
        except ValueError:
            # 日期如果在 holiday 中
            start_day = delta_date(start_day)
    delay_day_index = start_day_index + delta_day

    c = 1
    while 1:
        if delay_day_index < len(year_days):
            delay_day = year_days[delay_day_index]
            return delay_day
        nex_year = datetime.datetime.now().year + c
        nex_year_days = get_year_days(nex_year)
        if skip_holiday:
            nex_holiday_days = holiday_days or get_holiday_days(year)
            nex_year_days = difference_days(nex_year_days, nex_holiday_days)
        year_days = union_days(year_days, nex_year_days)
        c += 1


def print_today_year_calendar():
    """
    # >>> import calendar
    # >>> import datetime
    # >>> today_year = datetime.datetime.now().year
    # >>> print(calendar.calendar(today_year))
    :return:
    """
    today_year = datetime.datetime.now().year
    print(calendar.calendar(today_year))


if __name__ == '__main__':
    # get_year_days()
    print(get_week())
    print(get_week('2019-10-20'))
    print(delta_date('2019-11-24', 10))
    print(get_delta_date(10))  # 不指定日期
    print(get_delta_date(10, '2018-11-24'))  # 去年
    print(get_delta_date(10, '2019-11-24'))  # 跨月
    print(get_delta_date(20, '2019-12-24'))  # 跨年
    print(get_delta_date(396, '2019-12-24'))  # 跳年
    print(get_delta_date(10, '2019-11-24', True))  # 跳过节假日
    # print_today_year_calendar()
