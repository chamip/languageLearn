from random import randint


class Die():
    """模拟掷骰子的过程"""

    def __init__(self, num_sides=6):
        """初始化骰子面数"""
        self.num_sides = num_sides

    def roll(self):
        """掷骰子"""
        return randint(1, self.num_sides)

