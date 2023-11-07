from selenium import webdriver

from selenium.webdriver.common.by import By

import time

class Execute_JavaScript:
    def Demo(self):
        drive = webdriver.Chrome()
        drive.get("https://pythonbasics.org")
        js = 'alert("Hello World")'
        drive.execute_script(js)
      
        time.sleep(4)

demo = Execute_JavaScript()
demo.Demo()

