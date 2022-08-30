"""Honda Class contains all functions of Honda Car"""
from car import Car


class Honda(Car):
    """Class of Honda which extends car """
    def __init__(self, fuel_type: str, passenger_capacity):
        Car.__init__(self)
        self.fuel_type = fuel_type
        self.passenger_capacity = passenger_capacity

    def get_passenger_capacity(self):
        """Function to return passenger capacity"""
        return self.passenger_capacity

    def get_fuel_type(self):
        """Function to return fuel type"""
        return self.fuel_type

    def check_pressure(self, pressure: int):
        """Implementation of Abstract Function to check the pressure level of vehicle"""
        if pressure < 25:
            print('Warning : Pressure of Honda Vehicle is below 25')
        else:
            print('Honda is all good with pressure')

    def doors_closed(self, closed_doors: int = 4):
        """Implementation of Abstract Function to check whether the doors are closed or open"""
        if closed_doors < 4:
            print('Warning : Honda Vehicle has some doors opened')
        else:
            print('Honda vehicle has all doors closed')

    def fuel_check(self, fuel: int):
        """Implementation of Abstract Function to check the fuel capacity"""
        if fuel/100 < 0.05:
            print('Warning : Fuel level of Honda is low below 5%')
        else:
            print('You have enough fuel in Honda Vehicle')

    def open_rear_view_mirror(self, choice: str):
        """Implementation of abstract function to open rearview mirror"""
        if 'yes' in choice.lower():
            print('Opening rear view mirror of Honda')
        else:
            print('Honda has all mirror closed')

    def clean_win_shield(self, choice: str):
        """Implementation of function to clean the win-shield"""
        if 'yes' in choice.lower():
            print('You cleaned the win-shield of Honda')
        else:
            print('You did not cleaned the win-shield of Honda')
