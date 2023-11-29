from selenium import webdriver
from selenium.webdriver.common.by import By
import customChrome
import time

class Login:
    def TCLogin(self):
        for i in range(1,4):
            driver = customChrome.chrome_setup()
            driver.find_element(By.XPATH, "//table//tbody//tr["+ str(i) +"]").click()
            driver.find_element(By.XPATH, "//form[@id='loginForm']//button").click()
            js = "return window.location.href;"
            role = driver.execute_script(js)
            
            if role == "https://saleserpnew.bdtask.com/saleserp_v9.8_demo/home":
                print("- TC Login 01: Role Admin => Pass")
            elif role == "https://saleserpnew.bdtask.com/saleserp_v9.8_demo/gui_pos" and i == 2:
                print("- TC Login 02: Role Manager => Pass")
            elif role == "https://saleserpnew.bdtask.com/saleserp_v9.8_demo/gui_pos" and i == 3:
                print("- TC Login 03: Role Sales Counter => Pass")
            else:
                print("- TC Login 04: Check this case again => Fail")
            driver.delete_all_cookies()
            driver.quit()
 