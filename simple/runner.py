import unittest
from test_cases import TestCases

suite = unittest.TestSuite()
loader = unittest.TestLoader()
cases = loader.loadTestsFromTestCase(TestCases)
suite.addTest(cases)

runner = unittest.TextTestRunner()
runner.run(suite)
