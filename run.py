#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run.py
@time: 2019-11-22 17:48
"""

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from run_apps import app, host, port

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port, address=host)
IOLoop.instance().start()
