from selenium import webdriver

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
achains = ActionChains(driver)

# right click
# elm1 = driver.find_element(By.CSS_SELECTOR, 'span[class="context-menu-one btn btn-neutral"]')
# copy_elm1 = driver.find_element(By.XPATH, "//span[contains(text(), 'Copy')]")
# achains.context_click(elm1).perform()
# copy_elm1.click()
# time.sleep(2)

# double click
elm2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Double-Click Me To See Alert')]")
achains.double_click(elm2).perform()
time.sleep(4)


