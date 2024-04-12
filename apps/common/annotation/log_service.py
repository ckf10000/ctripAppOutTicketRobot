# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     log_service.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import traceback
import logging.config
from functools import wraps
import airtest.utils.logger

from apps.common.libs.parse_yaml import ProjectConfig

logging_plus = getattr(ProjectConfig.get_object(), "logging")
logging.config.dictConfig(logging_plus)
logger = logging.getLogger("root")


def auto_log(func):
    """
    自动打印日志
    :param func:
    :return:
    """

    @wraps(func)
    def _deco(*args, **kwargs):
        try:
            real_func = func(*args, **kwargs)
            return real_func
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(e)

    return _deco


# 源码中的logger配置，写死为debug级别，需要重置源码配置，让配置文件接管
airtest.utils.logger.init_logging = lambda: logging.getLogger("airtest")
airtest.utils.logger.init_logging()
