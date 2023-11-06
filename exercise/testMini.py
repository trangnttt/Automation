from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 

def customChrome():
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    print("[Open browser] Open google chrome browser")
    browser.get("https://cms.anhtester.com/login")
    return browser

def Login(username, password):
    if username == "":
        print("Your username is Null !!!")
    elif password == "":
        print("Your password is Null !!!")
    else:
        browser.find_element(By.ID, "email").send_keys(username)
        time.sleep(2)
        browser.find_element(By.ID, "password").send_keys(password)
        browser.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg btn-block"]').click()
        js = "return window.location.href;"
        if browser.execute_script(js) == "https://cms.anhtester.com/admin":
            print("Login successfull")
        else:
            print("You username and password is invalid !!!")

def Customers():
    print("==== Customers ====")
    browser.find_element(By.XPATH, "//a//span[contains(text(),'Customers')]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//span[contains(text(),'Customer list')]").click()
    time.sleep(2)
    search = browser.find_element(By.ID, "search")
    search.send_keys("nhi")
    search.send_keys(Keys.ENTER)
    time.sleep(2)

    search_results = browser.find_element(By.XPATH, "//table//tbody//tr[1]//span[@class='aiz-square-check']")
    
    if not search_results.is_selected():
        search_results.click()
        print("checkbox is selected.")
    else:
        print("checkbox is already selected.")
    time.sleep(4)


if __name__ == '__main__':
    print("==== Begin Test ====")
    browser = customChrome()

    print("[Login] Test Login")
    datas = (
        ["", "123456"],
        ["admin@example.com", ""],
        ["admin@example.com", "123"],
        ["admin@example.com", "123456"],
    )
    for data in datas:
        tc1 = Login(data[0], data[1])       

    customers = Customers()