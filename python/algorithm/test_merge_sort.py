# FILEPATH: /Users/chamip/github/languageLearn/python/algorithm/test_merge_sort.py

import unittest
from merge_sort import MergeSort  # 假设你的归并排序类名为MergeSort

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.sorter = MergeSort()

    def test_k_merge_sort(self):
        """测试k_merge_sort函数"""
        test_data = [
            ([3, 2, 1, 5, 4], 2, [1, 2, 3, 4, 5]),
            ([6, 5, 4, 3, 2, 1], 3, [1, 2, 3, 4, 5, 6]),
            ([], 1, []),
            ([1], 1, [1]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        ]
        for arr, k, expected in test_data:
            with self.subTest(arr=arr, k=k):
                self.assertEqual(self.sorter.k_merge_sort(arr, k), expected)

if __name__ == '__main__':
    unittest.main()