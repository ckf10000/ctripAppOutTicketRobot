# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     environ.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import os

__all__ = ["get_env", "DEFAULT_ENV_TYPE", "ENV_TYPE"]

ENV_TYPE = ["production", "development", "sit", "pre", "uat"]
DEFAULT_ENV_TYPE = "development"


def get_env():
    # 操作系统需配置环境变量：ENV_TYPE，否则视为 development 环境
    env_type = os.getenv("ENV_TYPE")
    if not env_type:
        env_type = DEFAULT_ENV_TYPE
    return env_type
