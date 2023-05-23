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

        driver.get("https://courses.letskodeit.com/practice")
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0, 600)")
        time.sleep(2)
        element = driver.find_element(By.ID, "mousehover")
        # itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Reload']"
        try:
            action = ActionChains(driver)
            action.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            action.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover faild on element")


ff = MouseHovering()
ff.test1()
