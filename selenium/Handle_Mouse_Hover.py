from selenium import webdriver

from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
# more_btn = driver.find_element(By.XPATH, '//span[@class="more-arr"]')
# achains = ActionChains(driver)
# achains.move_to_element(more_btn).perform()
# time.sleep(3)
# driver.find_element(By.XPATH,"//span[contains(text(), 'Xplore')]").click()
# time.sleep(5)

# hover vào My Account -> click login
account = driver.find_element(By.ID, "userLoginBlock")
achains = ActionChains(driver)
achains.move_to_element(account).perform()
time.sleep(3)
driver.find_element(By.XPATH,'//a[@id="signInBtn"]').click()
time.sleep(5)


