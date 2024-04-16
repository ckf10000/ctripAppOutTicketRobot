# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     booking_services.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import time
import typing as t
from decimal import Decimal
from apps.common.annotation.log_service import logger
from apps.common.config.flight_ticket import airline_map
from apps.common.libs.date_extend import current_datetime_str
from apps.domain.services.app_ui_services import CtripAppService
from apps.application.validators.booking_validators import FlightTicketValidator

__all__ = ["booking_flight_ser"]


class BookingFlightService(object):

    @classmethod
    def loop_payment_account(cls, app: CtripAppService, pre_sale_amount: str, payment_pass: t.List) -> t.Tuple:
        is_payment_success = False
        is_payment_card = None
        for payment_info in payment_pass:
            payment_pass = payment_info.get("pay_key")
            payment_card = payment_info.get("pay_name")
            payment_type = payment_info.get("pay_type")
            if payment_type == "gift_card":
                is_wallet_usable, amount = app.is_wallet_usable()
                if is_wallet_usable is True and FlightTicketValidator.validator_payment_with_wallet(
                        pre_sale_amount=Decimal(pre_sale_amount), actual_amount=amount
                ) is True:
                    app.touch_wallet_payment()
                    app.select_gift_card(payment_method=payment_card)
                    app.touch_wallet_immediate_payment()
                    app.enter_payment_pass(payment_pass=payment_pass)
                    is_payment_complete = app.is_payment_complete()
                else:
                    continue
            else:
                app.touch_payment_method()
                app.select_payment_method(payment_method=payment_card)
                app.select_point_deduction()
                ticket_actual_amount = app.get_ticket_actual_amount()
                ticket_deduction_amount = app.get_ticket_deduction_amount()
                do_validator = FlightTicketValidator.validator_payment_with_deduction(
                    pre_sale_amount=Decimal(pre_sale_amount),
                    actual_amount=ticket_actual_amount,
                    deduction_amount=ticket_deduction_amount,
                )
                if do_validator is True:
                    app.touch_bank_card_payment()
                    app.enter_payment_pass(payment_pass=payment_pass)
                    is_payment_complete = app.is_payment_complete()
                    if is_payment_complete is False:
                        app.is_balance(payment_card=payment_card)
                else:
                    continue
            if is_payment_complete is True:
                is_payment_success = True
                is_payment_card = payment_card
                break
        return is_payment_success, is_payment_card

    @classmethod
    def booking_ctrip_app_special_flight_ticket(
            cls,
            pre_order_id: str,  # 预售订单id
            departure_city: str,  # 离开城市编号
            arrive_city: str,  # 抵达城市编号
            departure_time: str,  # 起飞时间
            arrive_time: str,  # 抵达时间
            pre_sale_amount: str,  # 预售金额
            flight: str,  # 航班编号
            passenger: str,  # 乘客
            age_stage: str,  # 乘客年龄阶段，儿童/成人
            card_id: str,  # 身份证号
            card_type: str,  # 证件类型
            internal_phone: str,  # 内部手机号码
            payment_pass: t.List,  # 银行里与支付密码的列表
            ctrip_username: str,  # 携程账号
            user_pass: str,  # 携程账号密码
            departure_city_name: str = "",  # 离开城市名
            arrive_city_name: str = "",  # 抵达城市名
            passenger_phone: str = ""  # 乘客手机号码
    ) -> t.Dict:
        result = dict()
        ac = airline_map.get(flight[:2].upper())
        logger.info("本次要预定的航班：{}，为<{}>的航班，起飞时间为：{}".format(
            flight, ac, departure_time))
        app = CtripAppService()
        app.device.wake()
        app.restart()
        time.sleep(8)
        app.hide_navigation_bar()
        app.touch_home()
        app.touch_flight_ticket()
        app.touch_special_flight_ticket()
        app.select_departure_city()
        app.enter_search_value(search_value=departure_city)
        app.select_search_result_first_city(select_value=departure_city)
        app.sumbit_search_result()
        app.select_arrive_city()
        app.enter_search_value(search_value=arrive_city)
        app.select_search_result_first_city(select_value=arrive_city)
        app.sumbit_search_result()
        app.select_trip_date()
        app.select_trip_expect_month(date_str=departure_time)
        app.select_trip_expect_day(date_str=departure_time)
        app.touch_only_query_some_day()
        app.touch_query_special()
        is_exist_flight = app.is_exist_flight_in_screen(flight=flight)
        if is_exist_flight is False:
            app.touch_flight_inland_single_list_filter()
            app.touch_clear_filter()
            app.touch_filter_departure_time()
            app.select_filter_departure_time_area(date_str=departure_time)
            app.touch_filter_airline()
            app.select_filter_airline_company(ac)
            app.touch_filter_submit_button()
        app.select_special_flight(flight=flight)
        special_flight_amount = app.get_special_flight_amount()
        if special_flight_amount <= Decimal(pre_sale_amount):
            is_direct_booking = app.is_direct_booking()
            if is_direct_booking is True:
                app.touch_direct_booking_button()
            else:
                app.touch_booking_the_second_button()
                app.touch_ordinary_booking_button()
            app.check_user_login(username=ctrip_username, password=user_pass)
            app.touch_more_passengers_button()
            app.touch_add_passengers_button()
            app.touch_passenger_card_type()
            if card_type not in ["身份证"]:
                raise ValueError("暂时还不支持证件类型为: <{}>的乘客预订机票".format(card_type))
            if age_stage not in ["成人"]:
                raise ValueError("暂时不支持儿童乘客预订机票")
            app.select_passenger_card_type(card_type=card_type)
            app.enter_passenger_card_id(card_id=card_id)
            app.enter_passenger_username(passenger=passenger)
            app.enter_passenger_phone_number(phone=internal_phone)
            app.submit_passenger_info()
            app.submit_passenger_info_confirm()
            app.add_passenger(passenger=passenger)
            app.select_insecure()
            app.touch_fill_order_next_step()
            is_duplicate_order = app.is_duplicate_order()
            if is_duplicate_order:
                logger.warning(is_duplicate_order)
            else:
                app.touch_select_service_no_need()  # 保障不需要
                app.touch_select_service_no_need()  # 预约不需要
                app.touch_to_payment()
                app.touch_insure_no()
                app.touch_read_agree()
                app.select_more_payment()
                is_payment_success, payment_method = cls.loop_payment_account(
                    app=app, pre_sale_amount=pre_sale_amount, payment_pass=payment_pass
                )
                if is_payment_success is True:
                    payment_amount = app.get_order_with_payment_amount()
                    app.touch_payment_complete()
                    app.close_coupon_dialog()
                    app.expand_order_detail()
                    app.touch_order_detail()
                    app.close_important_trip_guidelines()
                    order_id = app.get_flight_ticket_with_order_id()
                    itinerary_id = app.get_flight_ticket_with_itinerary_id()
                    result = dict(
                        pre_order_id=pre_order_id,
                        departure_city=departure_city,
                        arrive_city=arrive_city,
                        departure_time=departure_time,
                        pre_sale_amount=pre_sale_amount,
                        flight=flight,
                        passenger=passenger,
                        age_stage=age_stage,
                        card_type=card_type,
                        card_id=card_id,
                        internal_phone=internal_phone,
                        passenger_phone=passenger_phone,
                        ctrip_order_id=order_id,
                        payment_amount=str(payment_amount),
                        payment_method=payment_method,
                        itinerary_id=itinerary_id,
                        departure_city_name=departure_city_name,
                        arrive_city_name=arrive_city_name,
                        arrive_time=arrive_time,
                        ctrip_username=ctrip_username,
                        payment_time=current_datetime_str()
                    )
                    return result
        else:
            logger.warning(
                "当前查询最低票价为：{}，高于航班订单票价：{}，本次预定即将结束。".format(
                    special_flight_amount, pre_sale_amount
                )
            )
        return result


booking_flight_ser = BookingFlightService()
