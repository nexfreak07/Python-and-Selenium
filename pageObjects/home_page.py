from selenium.webdriver.common.by import By


class HomePage:

    # Creating constructor of Homepage and passing driver
    def __init__(self, driver):
        self.driver = driver # initializing the driver

    shop = (By.LINK_TEXT, "Shop") # Creating an object to find element

    def shopItems(self): # Functions that find elements and return that element to main e2e function
        return self.driver.find_element(*HomePage.shop) # * is used to treat variable shop as tuple