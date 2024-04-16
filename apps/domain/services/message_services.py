# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     message_services.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import typing as t
from apps.common.libs.extensions import executor
from apps.common.annotation.log_service import logger
from apps.infrastructure.middleware.mq import push_message_to_mq


class MQMessageService(object):

    @classmethod
    def push_ctrip_app_flight_ticket_order(cls, message: t.Dict) -> None:
        logger.info("开始往MQ推送携程机票订单信息：<{}>".format(message))
        push_message_to_mq(message=message)
        logger.info("消息已发送至MQ队列.")

    @classmethod
    def async_push_ctrip_app_flight_ticket_order(cls, message: t.Dict) -> None:
        executor.submit(cls.push_ctrip_app_flight_ticket_order, message=message)
