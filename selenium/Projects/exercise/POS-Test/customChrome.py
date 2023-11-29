
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    driver.get("https://saleserpnew.bdtask.com/saleserp_v9.8_demo/login")
    time.sleep(3)
    return driver

