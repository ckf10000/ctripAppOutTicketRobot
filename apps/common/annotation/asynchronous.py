# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     asynchronous.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import typing as t
from functools import wraps
from traceback import print_exc
from apps.common.libs.extensions import executor


def async_threading(func: t.Callable):
    """
    多线程异步执行
    :param func:
    :return:
    """

    def call_func(func_inner: t.Callable, *args, **kwargs):
        try:
            return func_inner(*args, **kwargs)
        except Exception as e:
            print_exc()
            return e

    @wraps(func)
    def _deco(*args, **kwargs):
        executor.submit(call_func, func, *args, **kwargs)
        return

    return _deco
