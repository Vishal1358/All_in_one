from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-error")

driver = webdriver.Chrome(executable_path = "C:\\chrome\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)