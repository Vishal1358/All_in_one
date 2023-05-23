import os
from selenium import webdriver

# It is Open in chrome browser
os.environ['PATH'] += r"C:\Users\lenovo\webdriver\chromedriver_win32 (2)"
driver = webdriver.Chrome()

# it is open firefox
# os.environ['PATH'] += r"C:\Users\lenovo\webdriver\geckodriver-v0.31.0-win64 (1)"
# driver = webdriver.Firefox()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/p/core-java-for-automation-testers-interview-programs")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
# driver.close()