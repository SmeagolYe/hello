import requests

class HttpRequest:
    """根据method发起http请求"""
    def http_request(self, method, url, params):
        if method.lower() == "get":
            try:
                response = requests.get(url, params)
            except Exception as e:
                print("get请求出错~")
                raise e
        elif method.lower() == "post":
            try:
                response = requests.post(url, params)
            except Exception as e:
                print("post请求出错~")
                raise e
        else:
            print("method值不对~")

        return response.json()