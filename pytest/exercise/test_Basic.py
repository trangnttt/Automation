import unittest
from selenium import webdriver

class VNTestersTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)
    def testPageTitle(self):
        self.driver.get("https://vntesters.com")
        # self.assertIn("Cộng Đồng Kiểm Thử Phần Mềm", self.driver.title)
        assert self.driver.title == "Cộng Đồng Kiểm Thử Phần Mềm"

if __name__ == "__main__":
    unittest.main()