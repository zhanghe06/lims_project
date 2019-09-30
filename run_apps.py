#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_apps.py
@time: 2019-09-27 12:51
"""


from apps import app

host = app.config.get('HOST')
port = app.config.get('PORT')
debug = app.config.get('DEBUG')

if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)
