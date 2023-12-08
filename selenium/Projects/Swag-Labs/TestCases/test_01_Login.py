from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

def customChrome():
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")
    return browser

class TestCaseLogin(unittest.TestCase):
    def test_case_01(self):
        browser = customChrome()
        browser.find_element(By.ID,"login-button").click()
        error = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error == "Epic sadface: Username is required"
        print("TC01: Login user and pass are null =>  pass")

    def test_case_02(self):
        browser = customChrome()
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        browser.find_element(By.ID,"login-button").click()
        error = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error == "Epic sadface: Username is required"
        print("TC02: Login user is null =>  pass")
     
    def test_case_03(self):
        browser = customChrome()
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        browser.find_element(By.ID,"login-button").click()
        error = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error == "Epic sadface: Password is required"
        print("TC03: Login pass is null =>  pass")
         
    def test_case_04(self):
        browser = customChrome()
        browser.find_element(By.ID,"user-name").send_keys("invalid_user")
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        browser.find_element(By.ID,"login-button").click()
        error = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error == "Epic sadface: Username and password do not match any user in this service"
        print("TC04: Login user is invalid =>  pass")

    def test_case_05(self):
        browser = customChrome()
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        browser.find_element(By.ID,"password").send_keys("invalid_pass")
        browser.find_element(By.ID,"login-button").click()
        error = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error == "Epic sadface: Username and password do not match any user in this service"
        print("TC05: Login pass is invalid =>  pass")

    def test_case_06(self):
        browser = customChrome()
        browser.find_element(By.ID,"user-name").send_keys("invalid_user")
        browser.find_element(By.ID,"password").send_keys("invalid_pass")
        browser.find_element(By.ID,"login-button").click()
        error = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error == "Epic sadface: Username and password do not match any user in this service"
        print("TC06: Login user and pass are invalid =>  pass")

    
    def test_case_07(self):
        browser = customChrome()
        browser.find_element(By.ID,"user-name").send_keys("locked_out_user")
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        browser.find_element(By.ID,"login-button").click()
        error = browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error == "Epic sadface: Sorry, this user has been locked out."
        print("TC07: Login locked out user =>  pass")

    def test_case_08(self):
        browser = customChrome()
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        browser.find_element(By.ID,"login-button").click()
        title = browser.find_element(By.XPATH,"//span[@class='title']").text
        assert title == "Products"
        print("TC08: Login user and pass are valid =>  pass")
        
if __name__ == "__main__":
    print("--------- Run Test Case Login ---------")
    unittest.main()