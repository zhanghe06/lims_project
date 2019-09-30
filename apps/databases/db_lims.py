#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: db_lims.py
@time: 2019-09-27 13:07
"""

from flask_sqlalchemy import SQLAlchemy

from apps import app

db_lims = SQLAlchemy(app)
