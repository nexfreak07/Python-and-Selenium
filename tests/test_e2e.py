import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkout_page import CheckoutPage
from utilities.BaseClass import BaseClass
from pageObjects.home_page import HomePage

# By Inheriting we are optimizing usage of fixture
class TestOne(BaseClass):

    def test_e2e(self, setup):

        homePage = HomePage(self.driver) # Creating object of Homepage to Find element
        homePage.shopItems().click() # After Finding the element clicking to it
        checkOutPage = CheckoutPage(self.driver)
        phones =  checkOutPage.getPhones()

        for phone in phones:
            phone_name = checkOutPage.getPhoneName().text
            if phone_name == 'Blackberry':
                phone.find_element(By.XPATH, 'div/button').click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "td button.btn.btn-success").click()

        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")
        self.verify_link_presence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()  # Question????????????

        # <div class="alert alert-success alert-dismissible" xpath="1">
        #         The Above Element has three class name ---> alert, alert-success and alert-dismissible
        # Among those any one can be used

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        success_text =  self.driver.find_element(By.CLASS_NAME, 'alert-success').text
        print(success_text)
        assert 'Success! Thank you! Your order will be delivered in next few weeks :-).' in success_text  # Question?????????????????


