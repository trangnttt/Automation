import unittest

from parameterized import parameterized
from steps.ReadDataTest import readDataTest
from steps.step_login import stepLogin
from verifys.Verify_login import verifyLogin
from utils.CustomChrome import customChrome
import HTMLTestRunner

dataTests = readDataTest().dataTestLogin()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = customChrome()
        self.browser.get("https://the-internet.herokuapp.com/login")

    def tearDown(self):
        self.browser.quit()

    @parameterized.expand(dataTests)
    def test_login(self, no, username, password, desireResult, desireMessage):
        stepLogin(self.browser).login(username, password)
        self.assertIn(desireMessage, verifyLogin(self.browser).login())

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="../reports"))

