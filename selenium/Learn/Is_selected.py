from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
driver.get('https://pythonexamples.org/tmp/selenium/index-22.html')
driver.maximize_window()
mycheckbox = driver.find_element(By.ID, 'cherry')
if not mycheckbox.is_selected():
    mycheckbox.click()
    print(f"{mycheckbox.get_attribute('value')} checkbox is selected.")
else:
    print(f"{mycheckbox.get_attribute('value')} checkbox is already selected.")
driver.quit()