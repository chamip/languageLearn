"""一组可用于表示电动汽车的类"""

from car import Car

class Battery():
    """Electric Car Battery"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")


class ElectricCar(Car):
    """Electric Car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# my_tesla = ElectricCar('tesla', 'model s', 2023)
# my_tesla.battery = Battery(200)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
