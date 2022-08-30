"""The parent car class of all the cars"""
from abc import ABC, abstractmethod


class Car(ABC):
    """Car is an Abstract class which has below abstract methods"""
    def __init__(self, doors: int = 4, wheels: int = 4, win_shield: int = 1,
                 rear_view_mirror: int = 2, odometer: float = 100):
        self.doors = doors
        self.wheels = wheels
        self.win_shield = win_shield
        self.rear_view_mirror = rear_view_mirror
        self.odometer = odometer

    @abstractmethod
    def check_pressure(self, pressure):
        """Abstract Function to check the pressure level of vehicle"""
        pass

    @abstractmethod
    def doors_closed(self, closed_doors: int = 4):
        """Abstract Function to check if all doors are closed or not"""
        pass

    @abstractmethod
    def fuel_check(self, fuel):
        """Abstract Function to check the fuel level"""
        pass

    @abstractmethod
    def open_rear_view_mirror(self, choice):
        """Abstract Function to open the rearview mirror"""
        pass

    @abstractmethod
    def clean_win_shield(self, choice: str):
        """Abstract Function to clean the win-shield"""
        pass
