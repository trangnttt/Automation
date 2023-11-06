from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
driver.set_window_size(500, 400)

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-22.html')
driver.maximize_window()
# Find checkbox element
mycheckbox = driver.find_element(By.ID, 'cherry')

# Take a screenshot
# driver.save_screenshot("screenshot-1.png")

# Select checkbox if not already selected
if not mycheckbox.is_selected():
    mycheckbox.click()
    print(f"{mycheckbox.get_attribute('value')} checkbox is selected.")
else:
    print(f"{mycheckbox.get_attribute('value')} checkbox is already selected.")

# Take a screenshot
# driver.save_screenshot("screenshot-2.png")

# Close the driver
driver.quit()