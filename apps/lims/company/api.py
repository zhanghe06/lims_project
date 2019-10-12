#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: api.py
@time: 2019-09-27 11:30
"""

import datetime

from apps.databases.db_lims import db_lims
from apps.maps.status_delete import STATUS_DEL_OK
from apps.models.model_lims import Company
from libs.db_orm_pk import DbInstance

db_instance = DbInstance(db_lims)


def get_company_row_by_id(company_id):
    """
    通过 id 获取信息
    :param company_id:
    :return: None/object
    """
    return db_instance.get_row_by_id(Company, company_id)


def get_company_row(*args, **kwargs):
    """
    获取信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return db_instance.get_row(Company, *args, **kwargs)


def get_company_rows(*args, **kwargs):
    """
    获取列表
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_rows(Company, *args, **kwargs)


def get_company_limit_rows_by_last_id(last_pk, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param last_pk:
    :param limit_num:
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_limit_rows_by_last_id(Company, last_pk, limit_num, *args, **kwargs)


def add_company(company_data):
    """
    添加信息
    :param company_data:
    :return: None/Value of user.id
    :except:
    """
    return db_instance.add(Company, company_data)


def edit_company(company_id, company_data):
    """
    修改信息
    :param company_id:
    :param company_data:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.edit(Company, company_id, company_data)


def delete_company(company_id, force=False):
    """
    删除信息
    :param company_id:
    :param force:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    if force:
        return db_instance.delete(Company, company_id)
    else:
        data = {
            'status_delete': STATUS_DEL_OK,
            'delete_time': datetime.datetime.now()
        }
        if isinstance(company_id, list):
            return db_instance.update_rows(Company, data, Company.id.in_(company_id))
        else:
            return db_instance.edit(Company, company_id, data)


def get_company_pagination(page=1, size=10, *args, **kwargs):
    """
    获取列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param size:
    :param args:
    :param kwargs:
    :return:
    """
    rows = db_instance.get_pagination(Company, page, size, *args, **kwargs)
    return rows


def delete_company_table():
    """
    清空表
    :return:
    """
    return db_instance.delete_table(Company)


def count_company(*args, **kwargs):
    """
    计数
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.count(Company, *args, **kwargs)
