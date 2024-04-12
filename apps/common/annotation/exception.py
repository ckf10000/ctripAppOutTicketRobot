# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     exception.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from functools import wraps
from airtest.core.error import *


def airtest_exception_format(func):
    """
    airtest测试框架异常捕获格式化
    :param func:
    :return:
    """

    @wraps(func)
    def _deco(*args, **kwargs):
        try:
            result = func(*args, **kwargs) or None
        except (AdbError, AdbShellError) as e:
            result = (e.stdout + e.stderr).decode()
        except AirtestError as e:
            result = e
        except TimeoutError as e:
            result = e
        return result

    return _deco
