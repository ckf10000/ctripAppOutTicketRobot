# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     extensions.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from multiprocessing.pool import ThreadPool
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPool(processes=10)
executor = ThreadPoolExecutor(100)
