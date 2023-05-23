from selenium import webdriver
# chrome driver
from selenium.webdriver.common.service import Service
# --Chrome
from selenium.webdriver.common.by import By
service_obj = Service("E:\\ChromeDriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#  // a[contains(@href,'shob')]     a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_element(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()