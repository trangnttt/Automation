
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
# driver.implicitly_wait(10)
mywait = WebDriverWait(driver, 10) # Explicit Wait
driver.get("https://www.google.com/")
driver.maximize_window()
search_box =  driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()
# time.sleep(5)

result_search = driver.find_element(By.XPATH, "//h3[text() = 'Selenium']")

mywait.until(EC.element_to_be_clickable(result_search))

# search_link = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text() = 'Selenium']")))
result_search.click()


# driver.find_element(By.XPATH, "//h3[text() = 'Selenium']").click()
driver.quit()