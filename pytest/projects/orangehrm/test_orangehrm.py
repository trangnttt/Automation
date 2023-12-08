from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


class TestOrangeHRM:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_homePageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        assert self.driver.title == "OrangeHRM"

    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert self.driver.title == "OrangeHRM"

# pytest -v --html=report.html
