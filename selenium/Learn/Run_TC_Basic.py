# pip3 install webdriver-manager --upgrade
from selenium import webdriver

# from webdriver_manager.firefox import GeckoDriverManager #dùng cho firefox

# drive = webdriver.Chrome(ChromeDriverManager().install())
drive = webdriver.Firefox()
drive.get("https://www.rcvacademy.com/")
drive.maximize_window()
print(drive.title)

# # selenium 4
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# option = webdriver.ChromeOptions()
# option.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
# driver.get('https://www.google.com/')