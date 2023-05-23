import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="C:/Users/lenovo/webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://www.facebook.com/")
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("8904556663")
driver.find_element(By.XPATH, "//html[@id='facebook']//input[@id='pass']").send_keys("Vishal#1358")
driver.find_element(By.TAG_NAME, "button").click()
driver.find_element(By.TAG_NAME, "image").click()
time.sleep(5)
print(driver)

