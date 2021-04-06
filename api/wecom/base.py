import requests
from api.utils.logger import logger


class Base:

    def __init__(self):
        self.base_url = "https://qyapi.weixin.qq.com"
        self.proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }
        self.session = requests.Session()
        self.access_token = self.get_access_token()
        self.session.params = {
            "access_token": self.access_token
        }

    def get_access_token(self):
        path = "/cgi-bin/gettoken"
        params = {
            "corpid": "ww2252fababfb37b4b",
            "corpsecret": "-_10nepjwy4uW2wTgxc8WJjNXcgBYnSTQ4O_6dRhbJA"
        }
        r = self.send_request("GET", f"{self.base_url}{path}", params=params)
        return r.json()["access_token"]

    def send_request(self, *args, **kwargs):
        logger.debug(f"Send HTTP Request: {args}, {kwargs}")
        response = self.session.request(*args, **kwargs)
        logger.debug(f"Response: {response.text}")
        return response
