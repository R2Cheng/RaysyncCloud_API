
import Base
import requests
import pytest
from api.OrderAPI import Order
import logging
import allure

class TestOrder:

    def setup_class(self):
        self.session = requests.Session()
        self.order = Order()


    def teardown_class(self):
        self.session.close()

    # allure标题-title
    @allure.story("用例--订单记录获取列表测试")
    # allure描述信息
    @allure.description("该用例是针对订单记录列表接口的测试")
    @pytest.mark.parametrize("info", Base.get_data("order", "recharge_list"))
    def test_get_recharge_list(self,info):
        logging.info("-----------------test case recharge list start-----------------")
        #请求业务
        response = self.order.get_recharge_list(self.session,info["pageNum"],info["status"])

        #断言业务
        assert info["status_code"] == response.status_code
        logging.info("APi_Code ==>> 期望结果：{}， 实际结果：{}".format(info["status_code"],response.status_code))

        assert info["message"]==response.json().get("msg")
        logging.info("APi_Message ==>> 期望结果：{}， 实际结果：{}".format(info["message"],response.json().get("msg")))

        logging.info("----------------------------------")

        logging.info("APi_data ==>> 实际结果：{}".format(response.json().get("data")))
        logging.info("-----------------test case recharge list stop-----------------")