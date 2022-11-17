import pytest
from BaseClass import BaseClass
from log_file import TestLog
from pages.search_page import SearchPage
from utils.ReadData import ReadData


class TestSearch(BaseClass, TestLog):
    search_data = ReadData(
        DATA_PATH="/Users/Akash.Dasgupta/PycharmProjects/SeleniumPython/test_data/search_page.json")

    def test_trip_types(self):
        trip_types: list = SearchPage(self.driver).get_trip_types()
        trips = self.search_data.read_data()['Trip Types']
        assert trip_types == trips
        log = self.get_logger()
        log.info('Trip Types Passed')

    def test_fare_types(self):
        fare_types: list = SearchPage(self.driver).get_fare_types()
        actual_fare_types = self.search_data.read_data()['Fare Types']
        assert fare_types == actual_fare_types
        log = self.get_logger()
        log.info('Fare Types Passed')

    @pytest.mark.parametrize("data", search_data.read_data()['search-data'])
    def test_search(self, data):
        page = SearchPage(self.driver)
        log = self.get_logger()
        page.wait_for_frame()
        page.click_trip_type(data['Trip Type'])
        page.select_dept_city(data['Onboard'])
        page.select_arrival_city(data['Destination'])
        page.select_departure_date(data['Departure Date'])
        page.select_arrival_date(data['Return Date'])
        page.click_travel_button(data['Passenger'])
        result_page = page.search_entities()
        result_page.click_for_extra_filters()
        result_page.print_airlines(data['Onboard'], data['Destination'])
        result_page.apply_filters(data['airline1'], data['airline2'])
        assert 2 == result_page.get_applied_filters()

        log.info(f"Search Passed for flight {data['Onboard']} ----> {data['Destination']}")
        result_page.get_flight_cards()
        url: str = page.get_current_page_url()
        assert url == data['url']
        page.driver.back()
