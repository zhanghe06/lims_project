#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apis.py
@time: 2019-09-30 21:06
"""

from flask_restful import Api

from apps.commons.exceptions import errors
from apps.lims.blueprints import bp_lims

api_lims = Api(bp_lims, errors=errors)
