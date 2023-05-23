import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# It is Open in Chrome browser
os.environ['PATH'] += r"C:\Users\lenovo\webdriver\chromedriver_win32"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Class-name, name, linkText
driver.find_element(By.NAME, "email").send_keys("vishalhirandagi33@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#  XPATH -> //tag-name[@attribute='value]-> //input[@type='submit]
#  CSS -> tag-name[attribute='value]-> input[type='submit], #id .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Vishal")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# static dropdown selector
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown select by value

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("VishalH")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
