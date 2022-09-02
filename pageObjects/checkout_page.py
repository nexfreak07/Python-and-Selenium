from selenium.webdriver.common.by import By


class CheckoutPage:

    phones = (By.XPATH, "//div[@class='card h-100']")

    phone_name = (By.XPATH, "//div[@class='card h-100']/div/h4/a")

    def __init__(self, driver):
        self.driver = driver

    def getPhones(self):
        return self.driver.find_elements(*CheckoutPage.phones)

    def getPhoneName(self):
        return self.driver.find_element(*CheckoutPage.phone_name)
