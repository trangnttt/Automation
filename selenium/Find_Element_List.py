from  selenium import webdriver

from selenium.webdriver.common.by import By
import time

class FindElementByList:
    def locate_list(self):
        drive = webdriver.Chrome()
        drive.get("https://secure.yatra.com/social/common/yatra/signin.html")
        drive.maximize_window()
        lista = drive.find_elements(By.TAG_NAME, "p")
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(4)

elm = FindElementByList()
elm.locate_list()