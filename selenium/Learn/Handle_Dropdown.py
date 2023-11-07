from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Handle_Dropdown:
    def Demo(self):
        drive = webdriver.Chrome()
        drive.get("https://www.salesforce.com/ap/form/signup/freetrial-sales/?d=jumbo1-btn-ft")
        dropdwn = drive.find_element(By.NAME, "UserTitle")
        dd = Select(dropdwn)

        dd.select_by_index(1)
        time.sleep(2)

        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(2)

        dd.select_by_value("CxO_General_Manager_AP")
        time.sleep(2)

demo = Handle_Dropdown()
demo.Demo()

