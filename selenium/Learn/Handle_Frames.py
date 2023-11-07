from selenium import webdriver

from selenium.webdriver.common.by import By
import time

class Handle_Frames:
    def Demo(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com")
        driver.find_element(By.LINK_TEXT, "Frames").click()
        driver.find_element(By.LINK_TEXT, "Nested Frames").click()
        driver.switch_to.frame("frame-bottom")
        print(driver.find_element(By.XPATH,"//body").text)
        driver.switch_to.default_content()
        time.sleep(4)
demo = Handle_Frames()
demo.Demo()