from selenium import webdriver
from selenium.webdriver.common.by import By
from customChrome import chrome_setup

from testLogin import Login
import time

class Search:
    def testSearch(self):
        driver = chrome_setup()
        driver.find_element(By.XPATH, "//table//tbody//tr[3]").click()
        driver.find_element(By.XPATH, "//form[@id='loginForm']//button").click()      
        driver.find_element(By.XPATH, "//input[@id='product_name']").send_keys("choco")
        time.sleep(3)

        # results =  driver.find_elements(By.XPATH, "//div[@id='product_search']//h3[@class='item-details-title']")

        results =  driver.find_elements(By.XPATH, "//div[@id='product_search']/div")
        for result in results:
            print(result.text)

search = Search()
search.testSearch()

