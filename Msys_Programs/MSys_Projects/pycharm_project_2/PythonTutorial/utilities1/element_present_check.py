from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utilities1.handy_wrappers import HandyWrappers


class ElementPresentCheck():

    def test(self):
        service_obj = Service("C:/Users/lenovo/webdriver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)
        driver.get("https://courses.letskodeit.com/practice")

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//input[@ID='name']", By.XPATH)
        print(str(elementResult2))

ff = ElementPresentCheck()
ff.test()