""" Tata Class contains all operations of Tata """
from car import Car


class Tata(Car):
    """Class of Tata which extends car"""
    passenger_capacity = 5

    def __init__(self, color: str):
        Car.__init__(self)
        self.color = color

    def get_color(self):
        """Function to return the color of Vehicle"""
        return self.color

    def check_pressure(self, pressure: int):
        """Implementation of Abstract Function to check the pressure level of vehicle"""
        if pressure < 25:
            print('Warning : Pressure of Tata Vehicle is below 25')
        else:
            print('Tata is all good with pressure')

    def doors_closed(self, closed_doors: int = 4):
        """Implementation of Abstract Function to check whether the doors are closed or open"""
        if closed_doors < 4:
            print('Warning : Tata Vehicle has some doors opened')
        else:
            print('Tata vehicle has all doors closed')

    def fuel_check(self, fuel: int):
        """Implementation of Abstract Function to check the fuel capacity"""
        if fuel/100 < 0.05:
            print('Warning : Fuel level of Tata is low below 5%')
        else:
            print('You have enough fuel in Tata Vehicle')

    def open_rear_view_mirror(self, choice: str):
        """Implementation of abstract function to open rearview mirror """
        if 'yes' in choice.lower():
            print('Opening rear view mirror of Tata')
        else:
            print('Tata has all mirror closed')

    def clean_win_shield(self, choice: str):
        """Implementation of function to clean the win-shield"""
        if 'yes' in choice.lower():
            print('You cleaned the win-shield of Tata')
        else:
            print('You did not cleaned the win-shield of Tata')
