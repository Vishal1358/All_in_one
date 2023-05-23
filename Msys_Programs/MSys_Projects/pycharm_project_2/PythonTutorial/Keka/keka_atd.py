import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/web_driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://msys.keka.com/")

driver.maximize_window()
driver.implicitly_wait(10)

# Click on Login with Keka Password
driver.find_element(By.CSS_SELECTOR, "form[method='post'] > button:nth-of-type(2)").click()
time.sleep(2)

# Enter your msys email
driver.find_element(By.ID, "email").send_keys("vhirandagi@msystechnologies.com")
time.sleep(2)

# enter your Password
driver.find_element(By.ID, "password").send_keys("Vishal#1432")
time.sleep(2)

# click on login
driver.find_element(By.CSS_SELECTOR, ".btn.login-from-btn").click()
time.sleep(2)

# click on me button
me_button = driver.find_element(By.CSS_SELECTOR, ".ic-person")
me_button.click()
time.sleep(2)

# click on attendance
attendance = driver.find_element(By.LINK_TEXT, "ATTENDANCE")
attendance.click()
time.sleep(2)

# Select Work from home
wfh = driver.find_element(By.LINK_TEXT, "Work From Home")
wfh.click()
time.sleep(2)

# Selecting Dates
start_date = driver.find_element(By.CSS_SELECTOR, ".start-date .date-label")
start_date.click()
time.sleep(2)

date_f = driver.find_element(By.CSS_SELECTOR, "td:nth-of-type(2) > .custom-today-class.ng-star-inserted")
date_f.click()
time.sleep(2)
