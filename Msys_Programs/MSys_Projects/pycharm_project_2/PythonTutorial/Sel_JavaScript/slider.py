import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class MouseHovering():

    def test1(self):
        service_obj = Service("C:/Users/lenovo/webdriver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(2)

        driver.get("https://jqueryui.com/slider/")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, ".//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding Element Successful")
            time.sleep(2)
        except:
            print("Sliding failed on element")




ff = MouseHovering()
ff.test1()
