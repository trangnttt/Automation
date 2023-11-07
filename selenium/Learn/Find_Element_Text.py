from selenium import webdriver

from selenium.webdriver.common.by import By
import time

class FindElementText:
    def locate(self):
        drive = webdriver.Chrome()
        drive.get("https://www.yatra.com/")
        drive.maximize_window()
        Get_Txt = drive.find_element(By.XPATH, "//span[contains(text(),'Why book with Yatra.com?')]").text
        print(Get_Txt)

        Get_Attribute = drive.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input").get_attribute("value")
        print(Get_Attribute)
        time.sleep(4)

findID = FindElementText()
findID.locate()