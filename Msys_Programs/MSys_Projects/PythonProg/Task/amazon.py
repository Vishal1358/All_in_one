from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/web_driver/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://www.amazon.in/")

driver.maximize_window()
driver.implicitly_wait(15)

driver.find_element(By.CLASS_NAME,"nav-line-1-container").click()
driver.find_element(By.ID,"ap_email").send_keys("vishalhirandagi33@gmail.com")
driver.find_element(By.ID,"continue").click()
driver.find_element(By.NAME,"password").send_keys("Vishal#1432")
driver.find_element(By.ID,"signInSubmit").click()
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Dell laptop")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.CLASS_NAME, "s-image").click()
list_windows = driver.window_handles
driver.switch_to.window(list_windows[1])
driver.find_element(By.ID,"add-to-cart-button").click()
driver.find_element(By.ID, "attach-view-cart-button-form").click()
driver.find_element(By.ID,"desktop-ptc-button-celWidget").click()
driver.find_element(By.XPATH,'//*[@id="shipToThisAddressButton"]/span').click()
