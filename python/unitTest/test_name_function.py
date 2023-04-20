import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """name_function.py的单元测试"""

    def test_first_last_name(self):
        """测试处理包含名和姓参数"""
        formatted_name = get_formatted_name('taylor', 'swift')
        self.assertEqual(formatted_name, 'Taylor Swift')

    def test_first_last_middle_name(self):
        """测试包含中间名"""
        formatted_name = get_formatted_name('aaa', 'bbb', 'ccc')
        self.assertEqual(formatted_name, 'Aaa Ccc Bbb')


unittest.main()
