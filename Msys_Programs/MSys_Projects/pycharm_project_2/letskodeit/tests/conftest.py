import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        baseURL = "https://courses.letskodeit.com/"
        service_obj = Service("C:/Users/lenovo/firefox_driver/geckodriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on FF")
    else:
        baseURL = "https://courses.letskodeit.com/"
        service_obj = Service("C:/Users/lenovo/webdriver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.get(baseURL)
        print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
