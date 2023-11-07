from selenium import webdriver

from selenium.webdriver.common.by import By
from PIL import Image
import time

class Capture_Screenshot:
    def Demo(self):
        drive = webdriver.Chrome()
        drive.get("https://secure.yatra.com/social/common/yatra/signin.html")
        btn = drive.find_element(By.XPATH, '//button[@id="login-continue-btn"]')
        btn.screenshot("./selenium/test_img.png")
        btn.click()
        time.sleep(2)
        drive.get_screenshot_as_file("./Users/trangntt/Documents/Martha/Learns/selenium\\error.png")
        drive.save_screenshot("./selenium/test_img.png")
        screenshot = Image.open("./selenium/test_img.png")
        screenshot.show()
        time.sleep(4)

demo = Capture_Screenshot()
demo.Demo()

