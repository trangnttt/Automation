from selenium.webdriver.common.by import By
from pages.Page_login import *

class stepLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self, userName, passWord):
        self.inputUserName(userName)
        self.inputPassword(passWord)
        self.clickButtonLogin()


    def inputUserName(self, username):
        self.get_txtUserName().send_keys(username)

    def inputPassword(self, password):
        self.get_txtUserName().send_keys(password)

    def clickButtonLogin(self):
        self.get_btnLogin().click()



    
    def get_txtUserName(self):
        return self.drive.find_element(By.XPATH, txt_Username)

    def get_txtPassword(self):
        return self.drive.find_element(By.XPATH, txt_Password)
    
    def get_btnLogin(self):
        return self.drive.find_element(By.XPATH, btn_Login)