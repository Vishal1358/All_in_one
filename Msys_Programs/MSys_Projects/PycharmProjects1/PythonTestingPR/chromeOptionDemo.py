import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# It is Open in Chrome browser
os.environ['PATH'] += r"C:\Users\lenovo\webdriver\chromedriver_win32"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")