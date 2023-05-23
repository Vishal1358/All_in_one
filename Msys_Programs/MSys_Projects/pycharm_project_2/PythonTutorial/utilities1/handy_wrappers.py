from selenium.webdriver.common.by import By


class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "link_text":
            return By.LINK_TEXT
        elif locatorType == "tag_name":
            return By.TAG_NAME
        elif locatorType == "css_selector":
            return By.CSS_SELECTOR
        elif locatorType == "class_name":
            return By.CLASS_NAME
        else:
            print("Locator types is not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element not found")
        except:
            print("Element not found")
        return element

    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_elements(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")

        except:
            print("Element not found")
            return False
