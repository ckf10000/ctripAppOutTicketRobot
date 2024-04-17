# -*- coding: utf-8 -*-
"""
# -----------------------------------------------------------------------------------------------------------------------
# ProjectName:  smartIssueTickets
# FileName:     test_booking_services.py
# Description:  TODO
# Author:       ckf10000
# CreateDate:   2024/04/01 10:11:15
# Copyright ©2011-2024. Hunan xyz Company limited. All rights reserved.
# -----------------------------------------------------------------------------------------------------------------------
"""
from apps.application.services.booking_services import booking_flight_ser


def test_booking_ctrip_app_special_flight_ticket():
    booking_flight_ser.booking_ctrip_app_special_flight_ticket(
        departure_time="2024-04-13 21:50",
        departure_city="NKG",
        departure_city_name="南京",
        arrive_time="2024-04-13 23:30",
        arrive_city="CSX",
        arrive_city_name="长沙",
        flight="MF8036",
        passenger="李成浩",
        card_id="321284199803018015",
        card_type="身份证",
        pre_sale_amount="240.00",
        payment_pass=[{"card_type": "浦发银行储蓄卡(7397)", "pay_key": "901127"}],
        internal_phone="18569520328",
        passenger_phone="18261063386",
        age_stage="成人",
        pre_order_id="2891160",
        ctrip_username="18600440822",
        user_pass="ca161022"
    )


def test_check_user_login():
    from apps.domain.services.app_ui_services import CtripAppService
    app = CtripAppService()
    app.start()
    booking_flight_ser.check_user_login(app=app, username="18600440822", password="ca161022")


def test_loop_payment_account():
    from apps.domain.services.app_ui_services import CtripAppService
    app = CtripAppService()
    app.start()
    payment_pass = [
        {"card_type": "招商银行储蓄卡(1644)", "pay_key": "869182"}
    ]
    booking_flight_ser.loop_payment_account(app=app, pre_sale_amount="470.00", payment_pass=payment_pass)


if __name__ == "__main__":
    # test_booking_ctrip_app_special_flight_ticket()
    # test_loop_payment_account()
    test_check_user_login()
