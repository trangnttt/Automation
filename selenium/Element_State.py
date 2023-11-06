from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Element_State:
    def locate(self):
        drive = webdriver.Chrome()
        drive.get("https://training.openspan.com/login")
        drive.maximize_window()
        demo_state = drive.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)

        drive.find_element(By.NAME, "user_name").send_keys("admin")
        drive.find_element(By.XPATH, '//input[@id="user_pass"]').send_keys("test123")
        demo_state_1= drive.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state_1)

        time.sleep(4)

findID = Element_State()
findID.locate()