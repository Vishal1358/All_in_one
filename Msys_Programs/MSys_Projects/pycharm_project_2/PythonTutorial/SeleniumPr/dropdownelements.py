import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDown:

    def test(self):

        service_obj = Service("C:/Users/lenovo/webdriver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)

        driver.get("https://courses.letskodeit.com/practice")

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by Index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by Visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by Index")
        time.sleep(2)

ff = DropDown()
ff.test()