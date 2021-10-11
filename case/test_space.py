import requests
import Base
import pytest
import app
import logging
import allure
from api.SpaceAPI import Space


class TestSpace:

    def setup_class(self):
        self.session = requests.Session()
        self.space = Space()

    def teardown_class(self):
        self.session.close()

    # allure标题-title
    @allure.story("用例--我的空间获取用户信息测试")
    # allure描述信息
    @allure.description("该用例是针对我的空间获取用户信息接口的测试")
    @pytest.mark.parametrize("info", Base.get_data("space", "my_info"))
    def test_get_my_info(self,info):
        logging.info("-----------------test case my info start-----------------")
        # 请求业务
        response = self.space.get_my_info(self.session)

        # 断言业务
        assert info["status_code"] == response.status_code
        logging.info("APi_Code ==>> 期望结果：{}， 实际结果：{}".format(info["status_code"], response.status_code))

        assert info["message"] == response.json().get("msg")
        logging.info("APi_Message ==>> 期望结果：{}， 实际结果：{}".format(info["message"], response.json().get("msg")))
        logging.info("----------------------------------")

        logging.info("APi_data ==>> 实际结果：{}".format(response.json().get("data")))
        logging.info("-----------------test case my info stop-----------------")


    # allure标题-title
    @allure.story("用例--我的空间创建用户分享下载链接测试")
    # allure描述信息
    @allure.description("该用例是针对在我的空间创建用户分享下载链接接口的测试")
    @pytest.mark.parametrize("info", Base.get_data("space","share_add"))
    def test_share_add(self,info):
        logging.info("-----------------test case share add start-----------------")

        response = self.space.share_add(self.session,info["file"],info["shareType"],info["regionId"],info["fileType"],info["prefixUrl"],info["noticeEmail"],info["times"],info["noLogin"],info["emailContent"],info["expireTime"],info["size"])

        assert info["status_code"] == response.status_code
        logging.info("APi_Code ==>> 期望结果：{}， 实际结果：{}".format(info["status_code"], response.status_code))

        assert info["message"] == response.json().get("msg")
        logging.info("APi_Message ==>> 期望结果：{}， 实际结果：{}".format(info["message"], response.json().get("msg")))
        logging.info("-----------------test case share add stop-----------------")



if __name__ == '__main__':
    pytest.main(["-s", "test_space.py"])