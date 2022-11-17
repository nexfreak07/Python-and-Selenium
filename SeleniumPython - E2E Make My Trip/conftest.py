import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import locators


@pytest.fixture(scope='class')
def driver(request):
    service_obj = Service("/Users/Akash.Dasgupta/Documents/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.get(locators.url)
    request.cls.driver = driver
    yield
    driver.close()
