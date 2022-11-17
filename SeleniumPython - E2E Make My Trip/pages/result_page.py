from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils import extract
from utils import locators
from utils.data_class import Card
from selenium.webdriver.support import expected_conditions as es


class ResultPage:

    click = "arguments[0].click();"

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 5)

    def click_for_extra_filters(self):
        self.wait.until(es.visibility_of_element_located((By.XPATH, locators.wait_airlines)))
        self.driver.execute_script("window.scrollTo(0, 1200)")
        try:
            airlines = self.driver.find_element(By.XPATH, locators.more_airlines)
            self.driver.execute_script(self.click, airlines)
        except Exception as e:
            print(f'No Extra Filters : {e}')

    def print_airlines(self, dept, dest):
        self.wait.until(es.visibility_of_element_located((By.XPATH, locators.airlines_name)))
        names = self.driver.find_elements(By.XPATH, locators.airlines_name)
        print(f"Airline - {dept.upper()} ------> {dest.upper()}")
        print(f'Number of Airlines present are {len(names)}')
        print('Airlines name available are :')
        airlines_list = []
        for name in names:
            print('----------------------------')
            print(extract.format_airline(extract.extract_text(name.text)))
            airlines_list.append(extract.format_airline(extract.extract_text(name.text)))
            print('----------------------------')

    def apply_filters(self, airline1, airline2):
        career1 = f"//span[@title='{airline1}']/preceding-sibling::span[@class='customCheckbox']"
        filter1 = self.driver.find_element(By.XPATH, career1)
        self.driver.execute_script(self.click, filter1)

        career2 = f"//span[@title='{airline2}']/preceding-sibling::span[@class='customCheckbox']"
        self.wait.until(es.element_to_be_clickable((By.XPATH, career2)))
        self.driver.execute_script("window.scrollTo(0, 1220)")

        filter2 = self.driver.find_element(By.XPATH, career2)
        self.driver.execute_script(self.click, filter2)

    def get_applied_filters(self):
        self.wait.until(es.presence_of_element_located((By.XPATH, locators.applied_filters)))

        applied_filters = self.driver.find_elements(By.XPATH, locators.applied_filters)
        return len(applied_filters)

    def get_flight_cards(self):
        cards = self.driver.find_elements(By.XPATH, locators.search_card)

        print("Numer of Flight cards are ", len(cards))

        onboard_flight_cards = []
        return_flight_cards = []
        card_list = []
        for card in cards:
            card_list.append(Card(card))

        cities = self.driver.find_elements(By.XPATH, "(//p[text()='Flights from ' ]/b)")
        arr_city = cities[0].text
        dept_city = cities[1].text
        print(arr_city)
        print(dept_city)

        for i in range(0, len(card_list)):
            print('----------------------------------------------------------')
            print(f'Carrier name : {card_list[i].get_carrier_name()}')
            print(f'Departure City : {card_list[i].get_dept_city()}')
            print(f'Arrival City : {card_list[i].get_arr_city()}')
            print(f'Departure Time : {card_list[i].get_dept_time()}')
            print(f'Arrival Time : {card_list[i].get_arr_time()}')
            print(f'Total Time : {card_list[i].get_total_time()}')
            print(f'Layover : {card_list[i].get_layover()}')
            print(f'Fare : {card_list[i].get_fare()}')
            print('-----------------------------------------------------------')
            if card_list[i].get_dept_city() == arr_city:
                onboard_flight_cards.append(card_list[i])
            else:
                return_flight_cards.append(card_list[i])
