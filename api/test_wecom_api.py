import requests


class TestWecomApi:

    def setup(self):
        self.base_url = "https://qyapi.weixin.qq.com"
        self.proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }
        self.access_token = self.get_access_token()

    def get_access_token(self):
        path = "/cgi-bin/gettoken"
        params = {
            "corpid": "ww2252fababfb37b4b",
            "corpsecret": "-_10nepjwy4uW2wTgxc8WEHJuQ55bz0VM8yS8z97Pyo"
        }
        r = requests.get(f"{self.base_url}{path}", params=params)
        print(r.text)
        return r.json()["access_token"]

    def test_get_member_info(self):
        path = "/cgi-bin/user/get"
        params = {
            "access_token": self.access_token,
            "userid": "zhangsan"
        }
        r = requests.get(f"{self.base_url}{path}", params=params)
        print(r.text)
        assert r.json()["errcode"] == 0

    def test_creat_member(self):
        path = "/cgi-bin/user/create"
        params = {
            "access_token": self.access_token
        }
        data = {
            "userid": "mid",
            "name": "Mid",
            "mobile": "13300000000",
            "department": [1]
        }
        r = requests.post(f"{self.base_url}{path}", params=params, json=data)
        print(r.text)
        assert r.json()["errcode"] == 0

    def test_update_member(self):
        path = "/cgi-bin/user/update"
        params = {
            "access_token": self.access_token
        }
        data = {
            "userid": "mid",
            "name": "Mid-001"
        }
        r = requests.post(f"{self.base_url}{path}", params=params, json=data)
        print(r.text)
        assert r.json()["errcode"] == 0

    def test_delete_member(self):
        path = "/cgi-bin/user/delete"
        params = {
            "access_token": self.access_token,
            "userid": "mid"
        }
        r = requests.get(f"{self.base_url}{path}", params=params)
        print(r.text)
        assert r.json()["errcode"] == 0
