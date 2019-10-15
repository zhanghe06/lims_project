#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: operation_log.py
@time: 2019-10-12 16:56
"""

# from flask.signals import Namespace
from blinker import Namespace
from apps import app

_signal = Namespace()


signal_operation_log = _signal.signal('signal_operation_log')


@signal_operation_log.connect_via(app)
def operation_log(sender, **extra):
    """
    操作日志
    :param sender:
    :param extra:
    :return:
    """
    print(sender, extra)
