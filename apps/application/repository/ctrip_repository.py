# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     ctrip_repository.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import typing as t
from apps.common.libs.service_environ import configuration


class CTripConfigRepository(object):
    ctrip_config = getattr(configuration, "ctrip")
    payment_config = getattr(configuration, "fill_qlv")

    @classmethod
    def get_ctrip_group_config(cls, group_name: str) -> t.Dict:
        group_config = getattr(cls.ctrip_config, group_name)
        return dict(
            ctrip_username=getattr(group_config, "account"),
            user_pass=getattr(group_config, "sec_key"),
            payment_pass=getattr(group_config, "payment_type"),
            internal_phone=getattr(group_config, "internal_phone")
        )

    @classmethod
    def get_payment_group_config(cls, pay_method: str) -> t.Dict:
        fill_config = getattr(cls.payment_config, pay_method)
        return dict(
            out_pf=getattr(fill_config, "out_pf"),
            out_ticket_account=getattr(fill_config, "out_ticket_account"),
            pay_account_type=getattr(fill_config, "pay_account_type"),
            pay_account=getattr(fill_config, "pay_account")
        )

    @classmethod
    def get_passenger_info(cls, qlv_passengers: t.Dict) -> t.Dict:
        return dict(
            passenger=qlv_passengers.get("PName"),
            card_id=qlv_passengers.get("IDNo"),
            passenger_phone=qlv_passengers.get("Mobile"),
            age_stage=qlv_passengers.get("PType"),
            card_type=qlv_passengers.get("IDType")
        )
