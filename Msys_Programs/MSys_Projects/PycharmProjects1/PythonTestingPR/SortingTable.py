import os

from selenium import webdriver
from selenium.webdriver.common.by import By

BrowserSortedVeggieList = []
chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")
# It is Open in Chrome browser
os.environ['PATH'] += r"C:\Users\lenovo\webdriver\chromedriver_win32"
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# click column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all veggie name -> BrowserSortedVeggieList (A,B,C)
veggieWebElements = driver.find_element(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    BrowserSortedVeggieList.append(ele.text)

OriginalBrowserSortedList = BrowserSortedVeggieList.copy()

# sort this BrowserSortedVeggieList -> NewSortedList

BrowserSortedVeggieList.sort()

assert BrowserSortedVeggieList == OriginalBrowserSortedList
