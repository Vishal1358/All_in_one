from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(executable_path="D:\\Msys_Program\\Msys_Programs\\Web_driver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://keka.com//")
driver.close()
