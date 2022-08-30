"""Maruti Class contains all functions of Maruti Car"""
from car import Car


class Maruti(Car):
    """Class of Maruti which extends car"""
    passenger_capacity = 5

    def __init__(self, color: str, fuel_type: str):
        Car.__init__(self)
        self.color = color
        self.fuel_type = fuel_type

    def get_car_color(self):
        """Function to return color of the car"""
        return self.color

    def get_passenger_capacity(self):
        """Function to return passenger capacity"""
        return self.passenger_capacity

    def get_fuel_type(self):
        """Function to return fuel type"""
        return self.fuel_type

    def clean_win_shield(self, choice: str):
        """Implementation of function to clean the win-shield"""
        if 'yes' in choice.lower():
            print('Win-shield Cleaned of Maruti Vehicle')
        else:
            print('Win-shield not cleaned of Maruti Vehicle')

    def open_rear_view_mirror(self, choice):
        """Implementation of abstract function to open rearview mirror"""
        if 'yes' in choice.lower():
            print('Rear view mirror opened of Maruti Vehicle')
        else:
            print('Mirror not opened of Maruti Vehicle')

    def check_pressure(self, pressure):
        """Implementation of Abstract Function to check the pressure level of vehicle"""
        if pressure < 25:
            print('Warning: pressure below 25 of Maruti Vehicle')
        else:
            print('Maruti Vehicle has pressure above 25')

    def doors_closed(self, closed_doors: int = 4):
        """Implementation of Abstract Function to check whether the doors are closed or open"""
        if closed_doors < 4:
            print('Warning : Doors are opened of Maruti Vehicle')
        else:
            print('All Doors closed of maruti Vehicle')

    def fuel_check(self, fuel):
        """Implementation of Abstract Function to check the fuel capacity"""
        if fuel/100 < 0.05:
            print('Warning : Maruti Vehicle has Fuel below 5%')
        else:
            print('Maruti has good amount of fuel')
