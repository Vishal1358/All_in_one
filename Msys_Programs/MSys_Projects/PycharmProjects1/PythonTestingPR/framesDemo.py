import os

from selenium import webdriver
from selenium.webdriver.common.by import By

# It is Open in Chrome browser
os.environ['PATH'] += r"C:\Users\lenovo\webdriver\chromedriver_win32"
driver = webdriver.Chrome()
driver.implicitly_wait(2)


driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to call frame")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
