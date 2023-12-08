import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By


# Define test cases
class TestExample(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        self.driver = driver

    def test_search_google(self):
        driver = self.driver
        driver.get('https://google.com')
        search_box = driver.find_element(By.NAME,"q")
        search_box.send_keys('Selenium WebDriver')
        search_box.send_keys(Keys.ENTER)
        title = driver.title
        # self.assertEqual(title, 'Selenium WebDriver - Google Search')
        assert title == "Selenium WebDriver - Tìm trên Google"

    def tearDown(self):
        driver = self.driver
        driver.quit()

if __name__ == '__main__':
    # Create a test runner and generate HTML report
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestExample('test_search_google'))
    with open('report.html', 'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=open('report.html', 'w'),
            verbosity=2,
            title='Selenium WebDriver Test Report'
        )
        runner.run(test_suite)