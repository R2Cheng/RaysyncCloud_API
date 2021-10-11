import app
import allure


class Login:

    def __init__(self):
        self.login_url = app.BASE_URL + "/auth/login"


    #登录函数
    @allure.step("输入登录参数")
    def login(self,session,loginType,username,password):
        # my_login = {"mobile":mobile,
        #             "code":code}

        my_login = {}
        if loginType:
            my_login["loginType"] = loginType
        if username:
            my_login["username"] = username
        if password:
            my_login["password"] = password

        return session.post(self.login_url, json=my_login)

