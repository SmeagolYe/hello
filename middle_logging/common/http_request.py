import requests
import logging

class HttpRequest:
    """根据method发起http请求"""
    def http_request(self, method, url, params, cookies):
        if method.lower() == "get":
            try:
                response = requests.get(url, params, cookies=cookies)
            except Exception as e:
                logging.error("get请求出错~:{0}".format(e))
                raise e
        elif method.lower() == "post":
            try:
                response = requests.post(url, params, cookies=cookies)
            except Exception as e:
                logging.error("post请求出错~:{0}".format(e))
                raise e
        else:
            print("method值不对~")

        return response