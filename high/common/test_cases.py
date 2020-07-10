import unittest
import logging
from ddt import ddt, data
from common.read_excel import ReadExcel
from common.http_request import HttpRequest
from common import pro_path
from common import my_logger
from common.do_mysql import DoMysql

test_data = ReadExcel(pro_path.test_data_path).read_excel()
COOKIES = {} #全局变量cookie的初始值
LOAN_ID = "" #全局变量loanid的初始值
LOAN_MEMBER_ID = "110290" #借款用户的memberid
INVESTOR_ID = "" #投资人的id

@ddt
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.doExcel = ReadExcel(pro_path.test_data_path)

    @data(*test_data)
    def test_cases(self, item):
        global COOKIES #声明全局变量，必要的时候去更新cookie的值
        global LOAN_ID
        global INVESTOR_ID

        logging.info("正在执行第{0}条用例：{1}".format(item["case_id"], item["title"]))

        """在http请求之前，要完成item["param"]参数替换loan_id"""
        if item["params"].find("${loan_id}") != -1:
            new_param = item["params"].replace("${loan_id}", str(LOAN_ID))
            if new_param.find("${member_id}") != -1:
                new_param = new_param.replace("${member_id}", str(INVESTOR_ID))
        else:
            new_param = item["params"]

        response = HttpRequest().http_request(item["method"], item["url"], eval(new_param), COOKIES)

        """新注册的用户进行投资，所有需要放在请求之后，通过手机号去查询用户id"""
        if INVESTOR_ID == "":# 加这个判断是因为，前面几条用例都有mobilephone，且都是同样的mobilephone，所以只需要第一次替换就好
            query_investor_id = "select id from member where mobilephone = {0}".format(eval(item["params"])["mobilephone"])
            investor_id = DoMysql().do_mysql(query_investor_id)[0]
            INVESTOR_ID = investor_id

        """查询loan_id必须放在http请求之后"""
        query_loan_id = "select max(id) from loan where memberId = {0}".format(LOAN_MEMBER_ID)
        loan_id = DoMysql().do_mysql(query_loan_id)[0]

        if loan_id:# 当数据不为空的时候，进行数据替换
            LOAN_ID = loan_id

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

