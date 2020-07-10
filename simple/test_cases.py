import unittest
from ddt import ddt, data
from read_excel import ReadExcel
from http_request import HttpRequest

test_data = ReadExcel().read_excel()

@ddt
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        print("start start start")

    @data(*test_data)
    def test_cases(self, item):
        print("正在执行第{0}条用例：{1}".format(item["case_id"], item["title"]))
        response = HttpRequest().http_request(item["method"], item["url"], eval(item["params"]))
        try:
            self.assertEqual(response["code"], str(item["expected_code"]))
        except Exception as e:
            print("用例失败~")
            raise e

    def tearDown(self) -> None:
        print("stop stop stop")