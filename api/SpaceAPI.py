import app
import allure

class Space:

    def __init__(self):
        self.my_info_url = app.BASE_URL + "/user/get_my_info"
        self.share_add_url = app.BASE_URL + "/share/add"


    @allure.step("我的空间获取用户信息")
    def get_my_info(self,session):

        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer ",
            'token': app.TOKEN
        }

        return session.get(self.my_info_url,headers=my_headers)

    @allure.step("我的空间创建分享下载链接")
    def share_add(self,session,file,shareType,regionId,fileType,prefixUrl,size,noticeEmail,times,noLogin,emailContent,expireTime):

        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer ",
            'token': app.TOKEN
        }
        data = {}
        if file:
            data["file"] = file
        if shareType:
            data["shareType"] = shareType
        if regionId:
            data["regionId"] = regionId
        if fileType:
            data["fileType"] = fileType
        if prefixUrl:
            data["prefixUrl"] = prefixUrl
        if size:
            data["size"] = size
        if noticeEmail:
            data["noticeEmail"] = noticeEmail
        if times:
            data["times"] = times
        if noLogin:
            data["noLogin"] = noLogin
        if emailContent:
            data["emailContent"] = emailContent
        if expireTime:
            data["expireTime"] = expireTime

        return session.post(self.share_add_url,json = data ,headers = my_headers)
