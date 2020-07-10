import unittest
import HTMLTestRunner
from common.test_cases import TestCases
from common import pro_path
suite = unittest.TestSuite()
loader = unittest.TestLoader()
cases = loader.loadTestsFromTestCase(TestCases)
suite.addTest(cases)

# runner = unittest.TextTestRunner()

file = open(pro_path.test_report_path, "wb+")
runner = HTMLTestRunner.HTMLTestRunner(file, title="豆子来打羽毛球", description="高远球&平抽")
runner.run(suite)
