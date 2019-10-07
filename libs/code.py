#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: code.py
@time: 2019-10-07 23:41
"""


def gen_code_specimen():
    year_code = '2019'
    dep_code = 'FZ01'
    index_code = '000001'
    return 'NZJ(%s)%s-%s' % (year_code, dep_code, index_code)


if __name__ == '__main__':
    print(gen_code_specimen())
