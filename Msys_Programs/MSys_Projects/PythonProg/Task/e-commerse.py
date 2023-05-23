import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/web_driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(600)

driver.get("https://www.flipkart.com/")

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.flipkart.com");
driver.find_element(By.CLASS_NAME,"_2IX_2- VJZDxU").send_keys("vishalhirandagi33@gmail.com")
driver.find_element(By.XPATH("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")).sendKeys("Vishal#1358")
driver.find_element(By.XPATH("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button")).click()

