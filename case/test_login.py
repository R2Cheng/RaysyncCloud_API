# -*- coding: gbk -*-
import pytest
import requests
import app
from api.LoginAPI import Login
import Base
import os,sys
import logging
import allure

sys.path.append(os.getcwd())
class TestLogin:

    def setup_class(self):
        self.session = requests.Session()
        self.login_obj = Login()

    def teardown_class(self):
        self.session.close()

    # allure标题-title
    @allure.story("用例--登录测试")
    # allure描述信息
    @allure.description("该用例是针对登录接口的测试")
    @pytest.mark.parametrize("info", Base.get_data("login", "login_success"))
    def test_login(self,info):
        logging.info("-----------------test case login start-----------------")

        # 调用 api 的请求业务
        response = self.login_obj.login(self.session,info["loginType"],info["username"],info["password"])

        # 断言
        assert info["status_code"] == response.status_code
        logging.info("APi_Code ==>> 期望结果：{}， 实际结果：{}".format(info["status_code"],response.status_code))

        assert info["message"]==response.json().get("msg")
        logging.info("APi_Message ==>> 期望结果：{}， 实际结果：{}".format(info["message"],response.json().get("msg")))

        # 获取响应的身份标记: token
        app.TOKEN = response.json().get("data").get("token")
        logging.info("登录接口获取到用户{},的 token:{}".format(info["username"],app.TOKEN))

        logging.info("-----------------test case login stop-----------------")

    # 项目根目录执行生成报告
    # 生成allure报告：allure generate report/xml -o report/html --clean


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])