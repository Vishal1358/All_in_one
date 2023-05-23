import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers


class UsingWrappers():

    def test(self):
        service_obj = Service("C:/Users/lenovo/webdriver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)
        driver.get("https://courses.letskodeit.com/practice")

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()


ff = UsingWrappers()
ff.test()