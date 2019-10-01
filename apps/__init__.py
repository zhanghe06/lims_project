#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2019-09-27 11:25
"""

from flask import Flask

from apps.lims.apis import api_lims
from apps.lims.blueprints import bp_lims
from config import current_config

app = Flask(__name__)

# Load Config
app.config.from_object(current_config)

# Register Blueprint
app.register_blueprint(bp_lims)

# Add Resource Urls
from apps import urls
from apps.lims.applicant import url
from apps.lims.company import url
from apps.lims.contact import url
from apps.lims.department import url
from apps.lims.laboratory import url
from apps.lims.specimen import url
from apps.lims.user import url
