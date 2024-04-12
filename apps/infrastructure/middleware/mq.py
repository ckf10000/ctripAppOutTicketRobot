# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     mq.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import typing as t
from rabbitmq_plus.base.producer import Producer
from apps.common.config.parameters import rabbitmq_default_config as cfg


def push_message_to_mq(message: t.Any) -> None:
    producer = Producer(**cfg)
    producer.publish(message=message)
