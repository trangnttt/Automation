from selenium import webdriver

from selenium.webdriver.common.by import By
import time

drive = webdriver.Chrome()
drive.get("https://login.salesforce.com/")
drive.implicitly_wait(10)
drive.find_element(By.ID, "username").send_keys("admin")
drive.find_element(By.ID, "password").send_keys("123123")


time.sleep(4)