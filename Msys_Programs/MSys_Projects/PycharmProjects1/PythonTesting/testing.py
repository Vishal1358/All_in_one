from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
# service_obj = Service("C:\Users\lenovo\webdriver")
# driver = webdriver.Chrome(service=service_obj)

service_obj = Service("file:///C:/Users/lenovo/PycharmProjects1/PythonTesting/geckodr/geckodriver")
driver = webdriver.Firefox(service=service_obj)
print(driver.title)