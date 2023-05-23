import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/lenovo/webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://msys.keka.com/")

driver.maximize_window()
driver.implicitly_wait(10)

# Click on Login with Keka Password
driver.find_element(By.CSS_SELECTOR, "form[method='post'] > button:nth-of-type(2)").click()
time.sleep(1)

# Enter your msys email
driver.find_element(By.ID, "email").send_keys("vhirandagi@msystechnologies.com")
time.sleep(1)

# enter your Password
driver.find_element(By.ID, "password").send_keys("Vishal#1432")
time.sleep(1)

# click on login
driver.find_element(By.CSS_SELECTOR, ".btn.login-from-btn").click()
time.sleep(1)

# click on My finances
driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(5) > .nav-link").click()
time.sleep(2)

# click on My Pay
driver.find_element(By.LINK_TEXT, "MY PAY").click()
time.sleep(2)

# click on Pay Slips
driver.find_element(By.CSS_SELECTOR, ".sub-topnav [href='\#\/myfinances\/pay\/payslips']").click()
time.sleep(2)

# select month and click
driver.find_element(By.CSS_SELECTOR, ".list-group > a:nth-of-type(2)").click()
time.sleep(2)

# click on Download
driver.find_element(By.CSS_SELECTOR, "[class='ml-1']").click()
time.sleep(2)

month = driver.find_element(By.TAG_NAME, "h2").text
time.sleep(2)
# print(f"You Searched for this Month {month.text} Pay Slips {file.text}")

print(f"You searched for this Month {month}")

# driver.close()