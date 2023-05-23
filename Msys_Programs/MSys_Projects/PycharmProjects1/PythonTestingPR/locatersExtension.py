import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# It is Open in Chrome browser
os.environ['PATH'] += r"C:\Users\lenovo\webdriver\chromedriver_win32"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("vishalhirandagi33@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("123456789")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.find_element(By.XPATH, "//button[@text()='Save New Password]").click()
# driver.find_element(By.CLASS_NAME, "btn btn-custom btn-block").click()