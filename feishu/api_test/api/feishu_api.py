from feishu.api_test.api.base_api import BaseApi


class FeishuApi:
    """
    飞书的api公共特性，获取token，获取身份信息，断言请求结果（HTTP Code，status_code, msg）
    """

    def __init__(self):
        self.token = None

    def get_access_token(self):
        pass

    def check_response(self):
        pass
