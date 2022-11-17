from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.wait import WebDriverWait

from pages.result_page import ResultPage
from utils import locators



class SearchPage:
    click = "arguments[0].click();"

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 5)

    def click_trip_type(self, trip_type):  # Select Generic
        trip_types = f"//li[text()='{trip_type}']"
        trip = self.driver.find_element(By.XPATH, trip_types)
        self.action.click(on_element=trip).perform()

    def select_dept_city(self, departure_city_code):
        from_city = self.driver.find_element(By.XPATH, locators.from_city_button)
        self.action.click(on_element=from_city).perform()

        self.driver.find_element(By.XPATH, locators.from_city).clear()
        self.driver.find_element(By.XPATH, locators.from_city).send_keys(departure_city_code)
        onboard_city = f"//div[text()='{departure_city_code}']/ancestor::li[@role='option']"
        self.wait.until(es.presence_of_element_located(
            (By.XPATH, onboard_city)))

        departure = self.driver.find_element(By.XPATH, onboard_city)
        self.action.click(on_element=departure).perform()

    def select_arrival_city(self, arrival_city_code):
        to_city = self.driver.find_element(By.XPATH, locators.to_city_button)
        self.action.click(on_element=to_city).perform()

        self.driver.find_element(By.XPATH, locators.to_city).clear()
        self.driver.find_element(By.XPATH, locators.to_city).send_keys(arrival_city_code)

        arrival_city = f"//div[text()='{arrival_city_code}']/ancestor::li[@role='option']"
        self.wait.until(es.visibility_of_element_located((By.XPATH, arrival_city)))

        arrival = self.driver.find_element(By.XPATH, f"//div[text()='{arrival_city_code}']")
        self.driver.execute_script(self.click, arrival)

    def select_departure_date(self, dept_date):
        departure_date = self.driver.find_element(By.XPATH, locators.dept_button)
        self.driver.execute_script(self.click, departure_date)

        onboard_date = f"div[aria-label*='{dept_date}']"
        departure_date = self.driver.find_element(By.CSS_SELECTOR, onboard_date)
        self.driver.execute_script(self.click, departure_date)

    def select_arrival_date(self, arrival_date):
        date_of_arrival = f"div[aria-label*='{arrival_date}']"
        arr_date = self.driver.find_element(By.CSS_SELECTOR, date_of_arrival)
        self.driver.execute_script(self.click, arr_date)

    def click_travel_button(self, pax):
        travel_but = self.driver.find_element(By.CSS_SELECTOR, locators.travel_button)
        self.action.click(on_element=travel_but).perform()

        passenger = f"li[data-cy='adults-{pax}']"
        adult = self.driver.find_element(By.CSS_SELECTOR, passenger)
        self.action.click(on_element=adult).perform()

        apply_button = self.driver.find_element(By.CSS_SELECTOR, locators.apply)
        self.action.click(on_element=apply_button).perform()

    def search_entities(self):
        search = self.driver.find_element(By.CSS_SELECTOR, locators.search)
        self.action.click(on_element=search).perform()
        return ResultPage(self.driver)

    def get_trip_types(self):
        trips = "//span[@class='tabsCircle appendRight5']/parent::li"
        trip_types = self.driver.find_elements(By.XPATH, trips)
        trip_list = []
        for trip in trip_types:
            trip_list.append(trip.text)
        return trip_list

    def get_fare_types(self):
        fares = "//ul[@class='specialFareNew']/li/p"
        fare_types = self.driver.find_elements(By.XPATH, fares)
        fare_list = []
        for fare in fare_types:
            fare_list.append(fare.text)
        return fare_list

    def get_current_page_url(self):
        self.wait.until(es.visibility_of_all_elements_located((By.CSS_SELECTOR, ".journey-title")))
        return str(self.driver.current_url)

    def wait_for_frame(self):
        try:
            # frame = "//iframe[@name='notification-frame-~10cb47553']"
            # iframe = driver.find_element(By.XPATH, frame)
            # wait.until(es.frame_to_be_available_and_switch_to_it((By.XPATH, frame)))
            # driver.switch_to.frame(iframe)
            self.wait.until(es.presence_of_element_located((By.XPATH, "//i[@class='wewidgeticon we_close']")))
            cross = self.driver.find_element(By.XPATH, "//i[@class='wewidgeticon we_close']")
            self.driver.execute_script(self.click, cross)
            self.driver.switch_to.default_content()
        except Exception as e:
            print(' Element Not Found')
