# * Mở web -> Tạo class testLogin -> khởi tạo hàm có user, pass -> tạo hàm runTesst -> liệt kê các TH test
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import customChrome

class testLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def runTest(self):
        drive = customChrome.chrome_setup()
        drive.get("https://cms.anhtester.com/login")

        if self.username == "":
            print("Your username is Null !!!")
        elif self.password == "":
            print("Your password is Null !!!")
        else:
            drive.find_element(By.ID, "email").send_keys(self.username)
            time.sleep(2)
            drive.find_element(By.ID, "password").send_keys(self.password)
            drive.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg btn-block"]').click()
            js = "return window.location.href;"
            print(drive.execute_script(js))
            if drive.execute_script(js) == "https://cms.anhtester.com/admin":
                print("Login successfull")
            else:
                print("You username and password is invalid !!!")

tc1 = testLogin("admin@example.com", "123456")       
tc1.runTest()
tc2 = testLogin("", "123456")       
tc2.runTest()
tc3 = testLogin("admin@example.com", "")
tc3.runTest()
tc4 = testLogin("admin@example.com", "123")       
tc4.runTest()

