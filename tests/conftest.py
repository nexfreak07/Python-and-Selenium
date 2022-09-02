import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Command Line Hook to run tests in different browsers in PyTest - Runtime Variable
# first --browser_name is the keyvalue
# default is set as chrome
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )





@pytest.fixture(scope='class')
def setup(request):  # request is to send to the main file to handle the driver part

    browser = request.config.getoption('browser_name') # Configurattion to retrive value in the options
    if browser == 'chrome':
        service_obj = Service('/Users/Akash.Dasgupta/Documents/chromedriver')
        driver = webdriver.Chrome(service=service_obj)


    elif browser == 'firefox':
        print('Firefox Code')

    elif browser == 'IE':
        print('EDGE Code')

    driver.get('https://rahulshettyacademy.com/angularpractice')

    request.cls.driver = driver  # assigning the local driver of fixture to class driver
        # cls.driver is class driver
    yield
    driver.close()


