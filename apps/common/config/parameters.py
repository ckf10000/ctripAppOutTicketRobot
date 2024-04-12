# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     parameters.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
rabbitmq_default_config = {
    "port": 5672,
    "app_id": "smartIssueTickets",
    "host": "192.168.3.232",
    "username": "ticket",
    "password": "Admin@123",
    "virtual_host": "smartIssueTickets",
    "queue": "order.flight.ctrip",
    "exchange": "amq.fanout",
    "exchange_type": "fanout",
    "routing_key": ''
}