"""一个可模拟汽车的类"""

class Car():
    """一次模拟汽车的过程"""

    def __init__(self, make, model, year):
        """初始化"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回汽车的完整名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车的里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        """
        更新里程
        拒绝更新的里程数变小
        """
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("Don't roll back!")

    def increment(self, miles):
        """新增里程数"""
        self.odometer_reading += miles
