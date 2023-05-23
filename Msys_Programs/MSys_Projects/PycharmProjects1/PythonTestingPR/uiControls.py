import os

from selenium import webdriver
from selenium.webdriver.common.by import By

# It is Open in Chrome browser
os.environ['PATH'] += r"C:\Users\lenovo\webdriver\chromedriver_win32"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkboxe in checkboxes:
    if checkboxe.get_attribute("value") == "option2":
        checkboxe.click()
        assert checkboxe.is_selected()
        break

radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobutton[2].click()
assert radiobutton[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
