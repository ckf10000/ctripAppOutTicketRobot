# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     qlv_converter.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import typing as t
from decimal import Decimal
from apps.common.libs.date_extend import iso_to_standard_datestr


class QlvRequestParamsConverter(object):

    @classmethod
    def covert_flight_info(cls, order_id: int, flights: t.Dict) -> t.Dict:
        flight_info = dict(
            pre_order_id=order_id,
            departure_time=iso_to_standard_datestr(datestr=flights.get("DatDep"), time_zone_step=8),
            departure_city=flights.get("CodeDep"),
            departure_city_name=flights.get("CityDep"),
            arrive_time=iso_to_standard_datestr(datestr=flights.get("DatArr"), time_zone_step=8),
            arrive_city=flights.get("CodeArr"),
            arrive_city_name=flights.get("CityArr"),
            flight=flights.get("FlightNo"),
            pre_sale_amount=str(Decimal(flights.get("PriceStd")))
        )
        return flight_info
