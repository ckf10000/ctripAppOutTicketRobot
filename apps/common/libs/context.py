# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     context.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from typing import Any
from flask import current_app


def is_current_app() -> Any:
    try:
        with current_app.app_context():
            return True
    except RuntimeError:
        return False
