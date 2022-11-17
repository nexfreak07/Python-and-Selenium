from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Card:
    carrier_name = "descendant::span[@class='boldFont blackText']"
    departure_city = "descendant::div[@class='flexOne timeInfoLeft']/descendant::p[@class='blackText']"
    arrival_city = "descendant::div[@class='flexOne timeInfoRight']/descendant::p[@class='blackText']"
    departure_time = "descendant::div[@class='flexOne timeInfoLeft']/p[@class='appendBottom2 flightTimeInfo']/span"
    arrival_time = "descendant::div[@class='flexOne timeInfoRight']/p/span"
    total_time = "descendant::div[@class='stop-info flexOne']/p"
    layover = "descendant::div/p[@class='flightsLayoverInfo']"
    fare = "descendant::div[@class='makeFlex priceInfo gap-x-10 ']/div"

    def __init__(self, element: WebElement):
        self._parent = element

    def get_carrier_name(self):
        return str(self._parent.find_element(By.XPATH, self.carrier_name).text)

    def get_dept_city(self):
        return str(self._parent.find_element(By.XPATH, self.departure_city).text)

    def get_arr_city(self):
        return str(self._parent.find_element(By.XPATH, self.arrival_city).text)

    def get_dept_time(self):
        return str(self._parent.find_element(By.XPATH, self.departure_time).text)

    def get_arr_time(self):
        return str(self._parent.find_element(By.XPATH, self.arrival_time).text)

    def get_total_time(self):
        return str(self._parent.find_element(By.XPATH, self.total_time).text)

    def get_layover(self):
        return str(self._parent.find_element(By.XPATH, self.layover).text)

    def get_fare(self):
        return str(self._parent.find_element(By.XPATH, self.fare).text)

    def click_on_fare(self):
        return self._parent.find_element(By.XPATH, self.fare)
