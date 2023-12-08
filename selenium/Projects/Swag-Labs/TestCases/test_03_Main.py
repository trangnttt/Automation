from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains


def customChrome():
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID,"user-name").send_keys("standard_user")
    browser.find_element(By.ID,"password").send_keys("secret_sauce")
    browser.find_element(By.ID,"login-button").click()
    time.sleep(3)
    return browser

class TestCaseHeader(unittest.TestCase):
    def test_case_01(self):
        browser = customChrome() # login

        list_sort = ["Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)"]
        create_list_sort = []
        # active_option = browser.find_element(By.CLASS_NAME, "active_option") 
        options_sort = browser.find_elements(By.XPATH, "//select[@class='product_sort_container']//option")
        select_sort = browser.find_element(By.CLASS_NAME, "product_sort_container")
        option_chosse_sort = browser.find_element(By.XPATH, "//select[@class='product_sort_container']//option[2]")
        
        # check title 
        title = browser.find_element(By.XPATH, "//span[@class='title']")
        assert title.text == "Products"
        print("TC01: Check text Title =>    pass")

        # check data sort 
        
        assert browser.find_element(By.CLASS_NAME, "active_option").text == "Name (A to Z)"  #check text option default
        count_sort = len(options_sort)
        for i in range (1, count_sort+1):
            option_sort = browser.find_element(By.XPATH, "//select[@class='product_sort_container']//option["+ str(i) +"]")
            create_list_sort.append(option_sort.text)
        
        duplicates_found = False
        for element1 in list_sort:
            for element2 in create_list_sort:
                if element1 == element2:
                    duplicates_found = True
                    break
            if duplicates_found:
                break

        if duplicates_found == True:
            print("TC02: List data sort valid =>   pass")
        else:
            print("TC2: List data sort invalid =>  fail")

        # check select sort 
        select_sort.click()
        option_chosse_sort.click()
        time.sleep(6)
        assert browser.find_element(By.CLASS_NAME, "active_option").text == browser.find_element(By.XPATH, "//select[@class='product_sort_container']//option[2]").text
        print("TC3: check select sort =>    pass")

if __name__ == "__main__":
    print("--------- Run Test Case Header ---------")
    unittest.main()
        
        