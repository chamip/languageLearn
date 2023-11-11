# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr)//2]  # 选择中间的元素作为基准
#     left = [x for x in arr if x < pivot]  # 小于基准的元素
#     middle = [x for x in arr if x == pivot]  # 等于基准的元素
#     right = [x for x in arr if x > pivot]  # 大于基准的元素

#     return quick_sort(left) + middle + quick_sort(right)

# # 测试代码
# arr = [5, 3, 8, 6, 2, 7, 1, 4]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)  # 输出 [1, 2, 3, 4, 5, 6, 7, 8]

# # 在这个实现中，我们选择列表中间的元素作为基准值（pivot），
# # 然后将列表分成小于、等于和大于基准值的三个子列表。然后，
# # 我们递归地将子列表进行快速排序，直到子列表只有一个或没有元素。
# # 最后，将排序好的子列表按照顺序拼接起来得到最终的排序结果。

class QuickSort:
    def __init__(self) -> None:
        pass
    
    def quick_sort(self, arr:list)->list:
        n = len(arr)
        if n <= 1:
            return arr
        pivot = arr[n // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

if __name__ == '__main__':
    arr = [5, 3, 8, 6, 2, 7, 1, 4]
    qs = QuickSort()
    sorted_arr = qs.quick_sort(arr)
    print(sorted_arr)
