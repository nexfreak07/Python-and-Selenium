""" Final Class """
from maruti_car import Maruti
from honda_car import Honda
from tata_car import Tata


Ciaz = Maruti(color='Blue', fuel_type='Petrol')
Baleno = Maruti(color='Yellow', fuel_type='Petrol')
City = Honda(passenger_capacity=4, fuel_type='Petrol')
Brio = Honda(passenger_capacity=6, fuel_type='Diesel')
Harrier = Tata(color='Blue')


def start_car(choice):
    """ Function to start Car"""
    if 'ciaz' in choice:
        print('----------CIAZ-----------')
        print(f'Color of the ciaz is {Ciaz.get_car_color()}')
        print(f'Ciaz is of fuel type {Ciaz.get_fuel_type()}')
        print(f'Ciaz has passenger capacity {Ciaz.get_passenger_capacity()}')
        ciaz_engine: bool = bool(input('Enter to start ciaz engine'))
        start_ciaz(ciaz_engine)

    elif 'baleno' in choice:
        print('----------Baleno-----------')
        print(f'Color of baleno is {Baleno.get_car_color()}')
        print(f'Baleno is of fuel type {Baleno.get_fuel_type()}')
        print(f'Passenger capacity of Baleno is {Baleno.get_passenger_capacity()}')
        baleno_engine: bool = bool(input('Enter to baleno start engine'))
        start_baleno(baleno_engine)
    elif 'city' in choice:
        print('----------CITY-----------')
        print(f'Passenger capacity of City is {City.get_passenger_capacity()}')
        print(f'Fuel type of City is {City.get_fuel_type()}')
        print(f'City has {City.wheels} number of wheels')
        city_engine: bool = bool(input('Enter to city start engine'))
        start_city(city_engine)

    elif 'brio' in choice:
        print('----------BRIO-----------')
        print(f'Passenger capacity of Brio is {Brio.get_passenger_capacity()}')
        print(f'Brio has {Brio.get_fuel_type()} fuel type')
        print(f'Odometer of Brio has reached {Brio.odometer} kms')
        print(f'Brio has {Brio.doors} doors')
        brio_engine: bool = bool(input('Enter to brio start engine'))
        start_brio(brio_engine)

    elif 'harrier' in choice:
        print('----------HARRIER-----------')
        print(f'Harrier has {Harrier.passenger_capacity} passenger capacity')
        print(f'Color of Harrier is {Harrier.get_color()} ')
        harrier_engine: bool = bool(input('Enter to harrier start engine'))
        start_harrier(harrier_engine)


def start_ciaz(engine: bool):
    """ Function  to start engine of car ciaz"""
    if engine:
        print('----Starting Ciaz----\n')
        print('Engine Started of Ciaz')
        win_shield = (input('Enter Yes/No to clean Win-Shield of Ciaz'))
        Ciaz.clean_win_shield(win_shield)
        mirror = input('Enter choice for to open/close mirror yes/no of Ciaz')
        Ciaz.open_rear_view_mirror(mirror)
        pressure: int = int(input('Enter the tyres pressure of Ciaz'))
        Ciaz.check_pressure(pressure)
        doors: int = int(input('Enter number of doors closed of Ciaz'))
        Ciaz.doors_closed(doors)
        fuel: int = int(input('Enter fuel amount to check fuel of Ciaz'))
        Ciaz.fuel_check(fuel)
    else:
        print('Ciaz is Stopped, Turn the ignition on by passing True')


def start_baleno(engine):
    """ Function  to start engine of car baleno"""
    if engine:
        print('----Starting Ciaz----\n')
        print('Engine Started of Baleno')
        win_shield = (input('Enter Yes/No to clean Win-Shield of Baleno'))
        Baleno.clean_win_shield(win_shield)
        mirror = input('Enter choice for to open/close mirror yes/no of Baleno')
        Baleno.open_rear_view_mirror(mirror)
        pressure: int = int(input('Enter the tyres pressure of Baleno'))
        Baleno.check_pressure(pressure)
        doors: int = int(input('Enter number of doors closed of Baleno'))
        Baleno.doors_closed(doors)
        fuel: int = int(input('Enter fuel amount to check fuel of Baleno'))
        Baleno.fuel_check(fuel)
    else:
        print('Baleno is Stopped, Turn the ignition on by passing True')


def start_city(engine):
    """ Function  to start engine of car city"""
    if engine:
        print('----Starting City----\n')
        print('Engine Started of City')
        win_shield = (input('Enter Yes/No to clean Win-Shield of City'))
        City.clean_win_shield(win_shield)
        mirror = input('Enter choice for to open/close mirror yes/no of City')
        City.open_rear_view_mirror(mirror)
        pressure: int = int(input('Enter the tyres pressure of City'))
        City.check_pressure(pressure)
        doors: int = int(input('Enter number of doors closed of City'))
        City.doors_closed(doors)
        fuel: int = int(input('Enter fuel amount to check fuel of City'))
        City.fuel_check(fuel)
    else:
        print('City is Stopped, Turn the ignition on by passing True')


def start_brio(engine):
    """ Function  to start engine of car brio"""
    if engine:
        print('----Starting City----\n')
        print('Engine Started of Brio')
        win_shield = (input('Enter Yes/No to clean Win-Shield of Brio'))
        Brio.clean_win_shield(win_shield)
        mirror = input('Enter choice for to open/close mirror yes/no of Brio')
        Brio.open_rear_view_mirror(mirror)
        pressure: int = int(input('Enter the tyres pressure of Brio'))
        Brio.check_pressure(pressure)
        doors: int = int(input('Enter number of doors closed of Brio'))
        Brio.doors_closed(doors)
        fuel: int = int(input('Enter fuel amount to check fuel of Brio'))
        Brio.fuel_check(fuel)
    else:
        print('Brio is Stopped, Turn the ignition on by passing True')


def start_harrier(engine):
    """ Function  to start engine of car Harrier"""
    if engine:
        print('----Starting Harrier----\n')
        print('Engine Started of Harrier')
        win_shield = (input('Enter Yes/No to clean Win-Shield of Harrier'))
        Harrier.clean_win_shield(win_shield)
        mirror = input('Enter choice for to open/close mirror yes/no of Harrier')
        Harrier.open_rear_view_mirror(mirror)
        pressure: int = int(input('Enter the tyres pressure of Harrier'))
        Harrier.check_pressure(pressure)
        doors: int = int(input('Enter number of doors closed of Harrier'))
        Harrier.doors_closed(doors)
        fuel: int = int(input('Enter fuel amount to check fuel of Harrier'))
        Harrier.fuel_check(fuel)
    else:
        print('Harrier is Stopped, Turn the ignition on by passing True')


def main():
    """ Main method to start the car"""
    cars = ['ciaz', 'baleno', 'city', 'harrier', 'brio']
    while True:
        choice = input('Enter the car to ride [ciaz, baleno, city, harrier, brio]')
        if choice in cars:
            start_car(choice)
            break
        print('Invalid Car! No such car available ')


if __name__ == '__main__':
    main()
