from selenium import webdriver

from selenium.webdriver.common.by import By
import time

class Hidden_Elements:
    def locate(self):
        drive = webdriver.Chrome()
        drive.get("https://www.yatra.com/hotels")
        drive.maximize_window()
        drive.find_element(By.ID, "BE_Hotel_pax_info").click()
        drive.find_element(By.XPATH, '//div[@class="dflex pax-vol"]//div[3]//div//span[2]').click()
        elm = drive.find_element(By.XPATH,'//select[@class="ageselect"]').is_displayed()
        print(elm)
        time.sleep(4)

findID = Hidden_Elements()
findID.locate()