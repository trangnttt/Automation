from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoSelenium:
    def Browser_Commands(self):
        drive = webdriver.Chrome()
        drive.get("https://training.rcvacademy.com/")
        print(drive.current_url)
        print(drive.title)
        drive.maximize_window()
        drive.fullscreen_window()
        drive.refresh()
        drive.find_element(By.LINK_TEXT, 'ALL COURSES').click()
        drive.back()
        drive.forward()
        drive.minimize_window()
        time.sleep(4)
        drive.quit()

demo = DemoSelenium()
demo.Browser_Commands()

