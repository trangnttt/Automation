from selenium import webdriver

from selenium.webdriver.common.by import By
import time
# import Alert 
from selenium.webdriver.common.alert import Alert 


driver = webdriver.Chrome()

driver.get("https://ide.geeksforgeeks.org/tryit.php/WXYeMD9tD4") 

# create alert object 
alert = Alert(driver) 

# get alert text 
print(alert.text) 

# accept the alert 
alert.accept() 

# alert.dismiss() #loại bỏ alert có sẵn

time.sleep(4)