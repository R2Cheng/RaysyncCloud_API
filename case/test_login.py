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

    # allure����-title
    @allure.story("����--��¼����")
    # allure������Ϣ
    @allure.description("����������Ե�¼�ӿڵĲ���")
    @pytest.mark.parametrize("info", Base.get_data("login", "login_success"))
    def test_login(self,info):
        logging.info("-----------------test case login start-----------------")

        # ���� api ������ҵ��
        response = self.login_obj.login(self.session,info["loginType"],info["username"],info["password"])

        # ����
        assert info["status_code"] == response.status_code
        logging.info("APi_Code ==>> ���������{}�� ʵ�ʽ����{}".format(info["status_code"],response.status_code))

        assert info["message"]==response.json().get("msg")
        logging.info("APi_Message ==>> ���������{}�� ʵ�ʽ����{}".format(info["message"],response.json().get("msg")))

        # ��ȡ��Ӧ����ݱ��: token
        app.TOKEN = response.json().get("data").get("token")
        logging.info("��¼�ӿڻ�ȡ���û�{},�� token:{}".format(info["username"],app.TOKEN))

        logging.info("-----------------test case login stop-----------------")

    # ��Ŀ��Ŀ¼ִ�����ɱ���
    # ����allure���棺allure generate report/xml -o report/html --clean


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])