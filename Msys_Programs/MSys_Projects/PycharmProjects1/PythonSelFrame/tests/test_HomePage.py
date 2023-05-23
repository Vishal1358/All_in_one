import pytest
from HomePageData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, gatData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + gatData["firstname"])
        homepage.getName().send_keys(gatData["firstname"])
        homepage.getEmail().send_keys(gatData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), gatData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def gatData(self, request):
        return request.param
