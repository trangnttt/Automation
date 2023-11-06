from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://jqueryui.com/draggable/")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@class="demo-frame"]'))
elm1 = driver.find_element(By.ID, "draggable")
ActionChains(driver).drag_and_drop_by_offset(elm1, 50, 40).perform()

time.sleep(4)