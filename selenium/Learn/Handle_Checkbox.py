from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Handle_Checkbox:
    def locate(self):
        drive = webdriver.Chrome()
        drive.get("https://www.yatra.com/")
        drive.maximize_window()
        drive.find_element(By.ID, "special_student_offer").click()
        time.sleep(3)
        elm = drive.find_element(By.XPATH, '//li[@id="special_student_offer"]//i[@class="ico ico-checkbox ico-checkbox-checked"]').is_displayed()
        print(elm)

        time.sleep(3)
findID = Handle_Checkbox()
findID.locate()
