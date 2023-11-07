from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Auto_Suggestion:
    def Demo(self):
        drive = webdriver.Chrome()
        drive.get("https://www.yatra.com/")
        drive.maximize_window()
        depart_from = drive.find_element(By.XPATH, '//input[@id="BE_flight_origin_city"]')
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

        going_to = drive.find_element(By.XPATH, '//input[@id="BE_flight_arrival_city"]')
        going_to.send_keys("New")
        time.sleep(4)

        search_results = drive.find_elements(By.XPATH, '//div[@class="viewport"]//div[1]/li')
        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(4)
                break
        
        # # Handle Calendar
        drive.find_element(By.XPATH, '//input[@id="BE_flight_origin_date"]').click()
        time.sleep(4)
        # # Cách 1
        # drive.find_element(By.XPATH, '//td[@id="01/11/2023"]').click()
        # time.sleep(4)

        # # Cách 2
        all_dates = drive.find_elements(By.XPATH, '//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD"]')
        for date in all_dates:
            if date.get_attribute("data-date") == "04/11/2023":
                date.click()
                time.sleep(4)
                break

demo = Auto_Suggestion()
demo.Demo()

