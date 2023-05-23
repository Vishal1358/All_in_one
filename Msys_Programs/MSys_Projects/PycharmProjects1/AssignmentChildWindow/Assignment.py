from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions


service_obj = Service("C:/Users/lenovo/webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/loginpagePractise")

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

windowOpen = driver.window_handles
# print(windowOpen)
driver.switch_to.window(windowOpen[1])
email = driver.find_element(By.LINK_TEXT, "mailto:mentor@rahulshettyacademy.com").text
# print(email)

# driver.close()
driver.switch_to.window(windowOpen[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys('123456789')
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
driver.find_element(By.CSS_SELECTOR,'input[name="signin"]').click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//form/div)[1]")))
error_msg = driver.find_element(By.XPATH, "(//form/div)[1]").text
print(error_msg)