import unittest
import logging
from ddt import ddt, data
from common.read_excel import ReadExcel
from common.http_request import HttpRequest
from common import pro_path
from common import my_logger

test_data = ReadExcel(pro_path.test_data_path).read_excel()
COOKIES = {}

@ddt
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.doExcel = ReadExcel(pro_path.test_data_path)

    @data(*test_data)
    def test_cases(self, item):
        global COOKIES #声明全局变量，必要的时候去更新cookie的值

        logging.info("正在执行第{0}条用例：{1}".format(item["case_id"], item["title"]))
        response = HttpRequest().http_request(item["method"], item["url"], eval(item["params"]), COOKIES)
        """登录后会产生一个cookie，当cookie不为空时，就对全局变量进行修改"""
        if response.cookies != {}:
            COOKIES = response.cookies
        try:
            self.assertEqual(response.json()["code"], str(item["expected_code"]))
            result = "PASS"
        except Exception as e:
            logging.error("用例失败~:{0}".format(e))
            result = "FAIL"
            raise e
        finally:
            self.doExcel.write_back(item["case_id"] + 1, 7, str(response.json()), "test_data")
            self.doExcel.write_back(item["case_id"] + 1, 8, result, "test_data")


    def tearDown(self) -> None:
        print("stop stop stop")