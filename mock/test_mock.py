"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json
from mitmproxy import http


class Rewriter:

    def request(self, flow: http.HTTPFlow):
        # Record the request info and generate a python script
        if "qyapi.weixin.qq.com" in flow.request.pretty_url:
            url = flow.request.pretty_url
            method = flow.request.method
            headers = {}
            for key in flow.request.headers:
                headers[key] = flow.request.headers[key]
            headers = headers
            body = flow.request.content.decode("utf-8").replace("\"", "\\\"")

            with open("template", "r", encoding="utf-8") as f:
                template = f.read()
                script_text = template.format(url=url, method=method, headers=headers, data=body)

            with open("request_demo.py", "w", encoding="utf-8") as f:
                f.write(script_text)

        # Map local
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" in flow.request.pretty_url:
            with open("quote.json", "r", encoding="utf-8") as f:
                res_text = f.read()
            flow.response = http.HTTPResponse.make(content=res_text, headers={"Content-Type": "application/json"})

    def response(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" in flow.request.pretty_url:
            data = json.loads(flow.response.text)
            items = data["data"]["items"]
            item_count = len(items)

            # Set the percent to 0.01(red), 0(grey) and -0.01(green)
            for index in range(0, item_count):
                if index < item_count / 2:
                    items[index]["quote"]["percent"] = 0.01
                elif index == item_count / 2:
                    items[index]["quote"]["percent"] = 0
                elif index > item_count / 2:
                    items[index]["quote"]["percent"] = -0.01

            flow.response.text = json.dumps(data)


addons = [
    Rewriter()
]
