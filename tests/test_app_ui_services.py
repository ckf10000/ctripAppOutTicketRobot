# -*- coding: utf-8 -*-
"""
# -----------------------------------------------------------------------------------------------------------------------
# ProjectName:  smartIssueTickets
# FileName:     test_app_services.py
# Description:  TODO
# Author:       ckf10000
# CreateDate:   2024/04/01 11:14:51
# Copyright ©2011-2024. Hunan xyz Company limited. All rights reserved.
# -----------------------------------------------------------------------------------------------------------------------
"""
from apps.domain.services.app_ui_services import CtripAppService


def test_select_special_flight():
    app = CtripAppService()
    app.start()
    app.select_special_flight(flight="MF8266")


def test_select_insecure():
    app = CtripAppService()
    app.start()
    app.select_insecure()


def test_get_tickect_actual_amount():
    app = CtripAppService()
    app.start()
    app.get_ticket_actual_amount()


def test_get_tickect_deduction_amount():
    app = CtripAppService()
    app.start()
    app.get_ticket_deduction_amount()


def test_close_important_trip_guidelines():
    app = CtripAppService()
    app.start()
    app.close_important_trip_guidelines()


def test_get_flight_ticket_with_order_id():
    app = CtripAppService()
    app.start()
    print(app.get_flight_ticket_with_order_id())


def test_get_flight_ticket_with_itinerary_id():
    app = CtripAppService()
    app.start()
    print(app.get_flight_ticket_with_itinerary_id())


def test_select_more_payment():
    app = CtripAppService()
    app.start()
    app.select_more_payment()


def test_enter_payment_pass():
    app = CtripAppService()
    app.start()
    app.enter_payment_pass(payment_pass="0123456789")


def test_select_search_result_first_city():
    app = CtripAppService()
    app.start()
    app.select_search_result_first_city(select_value="PEK")


def test_close_coupon_dialog():
    app = CtripAppService()
    app.start()
    app.close_coupon_dialog()


def test_expand_order_detail():
    app = CtripAppService()
    app.start()
    app.expand_order_detail()


def test_touch_order_detail():
    app = CtripAppService()
    app.start()
    app.touch_order_detail()


def test_touch_passenger_card_type():
    app = CtripAppService()
    app.start()
    app.touch_passenger_card_type()


def test_select_passenger_card_type():
    app = CtripAppService()
    app.start()
    app.select_passenger_card_type(card_type="身份证")


def test_select_payment_method():
    app = CtripAppService()
    app.start()
    app.select_payment_method(payment_method="民生银行信用卡(6269)")


def test_select_point_deduction():
    app = CtripAppService()
    app.start()
    app.select_point_deduction()


def test_is_wallet_usable():
    app = CtripAppService()
    app.start()
    print(app.is_wallet_usable())


def test_touch_wallet_payment():
    app = CtripAppService()
    app.start()
    app.touch_wallet_payment()


def test_select_gift_card():
    app = CtripAppService()
    app.start()
    app.select_gift_card(payment_method="礼品卡-任我行")


if __name__ == "__main__":
    # test_select_special_flight()
    # test_select_insecure()
    # test_get_tickect_actual_amount()
    # test_get_tickect_deduction_amount()
    # test_close_important_trip_guidelines()
    # test_get_flight_ticket_with_order_id()
    # test_get_flight_ticket_with_itinerary_id()
    # test_select_more_payment()
    # test_enter_payment_pass()
    # test_select_search_result_first_city()
    # test_close_coupon_dialog()
    # test_expand_order_detail()
    # test_touch_order_detail()
    # test_touch_passenger_card_type()
    # test_select_passenger_card_type()
    # test_select_payment_method()
    # test_select_point_deduction()
    # test_is_wallet_usable()
    # test_touch_wallet_payment()
    test_select_gift_card()
