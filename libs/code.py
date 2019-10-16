#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: code.py
@time: 2019-10-07 23:41
"""

from string import digits, ascii_uppercase, ascii_lowercase
from itertools import product


def gen_code_specimen():
    year_code = '2019'
    dep_code = 'FZ01'
    index_code = '000001'
    return 'NZJ(%s)%s-%s' % (year_code, dep_code, index_code)


def gen_code_uppercase(c=2, m=1):
    # chars = digits + ascii_uppercase + ascii_lowercase
    chars = ascii_uppercase
    r = []
    for n in range(1, c + 1):
        for comb in product(chars, repeat=n):
            r.append(''.join(comb))
            if len(r) >= m:
                return r
    return r


if __name__ == '__main__':
    print(gen_code_specimen())
    print(gen_code_uppercase(m=2))
