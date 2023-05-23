import os

from selenium import webdriver
chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")
# It is Open in Chrome browser
os.environ['PATH'] += r"C:\Users\lenovo\webdriver\chromedriver_win32"
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")