import requests


def request_demo():
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
    param = {
        "access_token": "r6NyhzQ9jHjaNR4QRh0IUuc1H6rXHVhe8dCaj2_CR6BYYH0pMfp1SLUuhGaTXJ0Y2wKtn6usbizC2VuzYHetXvBuZSIUD"
                        "nM8KFQ0RT2QB0D_m0UOuz84F1iDd8-0ZXmW1Otx1tMilclWcKMQSR6qujaH3aQxNpFC0EsvSe1FWS2uBlcfEWZK-M28OM"
                        "9mwZHHfkCL55TfZDJW1Id9V6p8-Q"
    }
    data = {
        "userid": "mid",
        "name": "Mid",
        "mobile": "13300000000",
        "department": [1]
    }
    proxy = {
        "http": "http://127.0.0.1:8889",
        "https": "http://127.0.0.1:8889"
    }
    requests.post(url=url, params=param, json=data, proxies=proxy, verify=False)


if __name__ == '__main__':
    request_demo()
