from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Multiselect_List_Dropdown:
    def Demo(self):
        drive = webdriver.Chrome()
        drive.get("https://openwritings.net/sites/default/files/selenium-test-pages/select.html")
        dd_demo = drive.find_element(By.ID, 'multi-selections')
        dd_multi = Select(dd_demo)

        dd_multi.select_by_index(1)
        dd_multi.select_by_visible_text("March")
        dd_multi.select_by_value("Apr")
        
        # xoá cái đã chọn
        # dd_multi.deselect_by_index(0)
        # dd_multi.deselect_by_visible_text("March")
        # dd_multi.deselect_by_value("Apr")
        # dd_multi.deselect_all()
        time.sleep(4)

        

demo = Multiselect_List_Dropdown()
demo.Demo()

