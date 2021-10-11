"""
    封装请求业务:
        函数:获取频道列表的请求
"""
import app
import allure

class Order:
    def __init__(self):
        self.recharge_list_url = app.BASE_URL + "/recharge/list"


    # 获取订单记录
    @allure.step("输入页数和时间范围")
    def get_recharge_list(self,session,pageNum,status):

        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer ",
            'token': app.TOKEN
        }

        params= {}
        if pageNum:
            params["file"] = pageNum
        if status:
            params["shareType"] = status


        return session.get(self.recharge_list_url,headers=my_headers,params = params)

