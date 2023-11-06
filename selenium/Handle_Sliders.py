from selenium import webdriver

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.snapdeal.com/products/mobiles-printed-back-covers?sort=plrty")
driver.maximize_window()
elm1 = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
elm2 = driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
# ActionChains(driver).drag_and_drop_by_offset(elm1, 60, 0).perform()
# ActionChains(driver).click_and_hold(elm1).pause(1).move_by_offset(50,0).release().perform()
# ActionChains(driver).move_to_element(elm1).pause(1).click_and_hold(elm1).move_by_offset(80,0).release().perform()
ActionChains(driver).drag_and_drop_by_offset(elm2, -80, 0).perform()


time.sleep(4)