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
        display_menu = browser.find_element(By.XPATH,"//div[@class='bm-menu-wrap']")
        btn_menu = browser.find_element(By.ID,"react-burger-menu-btn")
        list_data_menu = ["All Items", "About", "Logout", "Reset App State"]
        create_data_menu_list = []

        # check display menu 
        assert display_menu.get_attribute("aria-hidden") == "true"
        print("TC01: Menu is enable =>    pass")
        btn_menu.click()
        assert  display_menu.get_attribute("aria-hidden") == "false"
        print("TC02: Menu is display =>   pass")
        btn_menu.click()

        # check count item menu 
        item_menu = browser.find_elements(By.XPATH,"//nav[@class='bm-item-list']//a")
        count_item_menu = len(item_menu)
        assert count_item_menu == 4
        print("TC03: Count item menu =>   pass")

        # check data item menu 
        btn_menu.click()
        time.sleep(4)
        for i in range (1, count_item_menu+1):
            item_menu_list = browser.find_element(By.XPATH,"//nav[@class='bm-item-list']//a["+str(i)+"]")
            create_data_menu_list.append(item_menu_list.text)

            # check hover menu
            achains = ActionChains(browser)
            achains.move_to_element(item_menu_list).perform()
            
        duplicates_found = False
        for element1 in list_data_menu:
            for element2 in create_data_menu_list:
                if element1 == element2:
                    duplicates_found = True
                    break
            if duplicates_found:
                break

        if duplicates_found == True:
            print("TC04: List data menu valid and hover menu =>   pass")
        else:
            print("TC04: List data menu invalid or hover menu =>  fail")

        # check logo
        logo = browser.find_element(By.CLASS_NAME,"app_logo")
        assert logo.text == "Swag Labs"
        print("TC05: Check Text Logo =>   pass")

        # # check default cart
        cart = browser.find_elements(By.XPATH,"//a[@class='shopping_cart_link']//span")
        assert  len(cart) == 0
        print("TC06: Check default count cart => pass")

        # check cart > 0
        browser.find_element(By.XPATH,"//div[@class='inventory_list']//div[@class='inventory_item'][1]//button").click()
        cart = browser.find_elements(By.XPATH,"//a[@class='shopping_cart_link']//span")
        assert  len(cart) > 0
        print("TC07: Check cart has product=> pass")
      

if __name__ == "__main__":
    print("--------- Run Test Case Header ---------")
    unittest.main()
        