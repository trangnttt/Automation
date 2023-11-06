# Viết code class FindElementByIDandName => phương thức locate_by_id tìm ID và Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FindElement:
    def locate(self):
        drive = webdriver.Chrome()
        drive.get("https://secure.yatra.com/social/common/yatra/signin.html")
        drive.maximize_window()
        
        # ID_Elm = drive.find_element(By.ID, "login-input") # tìm ID
        # ID_Elm = drive.find_element(By.NAME, "login-input") # tìm NAME 
        # ID_Elm = drive.find_element(By.XPATH, "//input[@name='login-input']") #tìm XPATH
        # ID_Elm =  drive.find_element(By.CSS_SELECTOR, "#login-input") # tìm CSS_SELECTOR 
        # ID_Elm =  drive.find_element(By.TAG_NAME, "input") # tìm CSS_SELECTOR 
        ID_Elm =  drive.find_element(By.CLASS_NAME, "email-login-box") # tìm CSS_SELECTOR 
        ID_Elm.send_keys("admin")
        # Link_Txt = drive.find_element(By.LINK_TEXT, "Terms of Service").click() # tìm LINK TEXT
        Partial_Link_Txt = drive.find_element(By.PARTIAL_LINK_TEXT, "Terms of").click() # tìm PARTIAL LINK TEXT
       
        time.sleep(4)

findID = FindElement()
findID.locate()