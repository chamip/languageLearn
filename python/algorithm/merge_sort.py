import heapq

class MergeSort:
    def __init__(self) -> None:
        pass

    def merge(self, arrays:list):
        heap = []
        result = []
        
        # 初始化堆
        for i in range(len(arrays)):
            if len(arrays[i]) > 0:
                heapq.heappush(heap, (arrays[i][0], i))
                arrays[i] = arrays[i][1:]  # 子数组指针后移
        
        # 多路归并排序
        while heap:
            val, index = heapq.heappop(heap)
            result.append(val)
            
            if len(arrays[index]) > 0:
                heapq.heappush(heap, (arrays[index][0], index))
                arrays[index] = arrays[index][1:]
                
        return result

    def k_merge_sort(self, arr:list, k:int):
        if len(arr) <= 1:
            return arr
        n = len(arr)
        step = (n + k - 1) // k
        parts = [arr[i:i+step] for i in range(0, n, step)]  # 将数组分成k个部分
        sorted_parts = []
        for part in parts:
            sorted_part = self.k_merge_sort(part, k)  # 递归对每个部分进行排序
            sorted_parts.append(sorted_part)
        #print("sorted_parts: ", sorted_parts)
        return self.merge(sorted_parts)  # 合并k个有序数组

if __name__ == '__main__':
    arrays = [7,3,10,6,2,4,8,1,5,9,11,12,0]
    m = MergeSort()
    res = m.k_merge_sort(arrays, 3)
    print(res)
    #print(k_merge_sort(arrays, 3))  # 输出：[1, 2, 3, 4, 5, 7, 8, 9, 10]
    # arrays = [
    #     [3, 7, 10],
    #     [2, 4, 8],
    #     [1, 5, 9]
    # ]
    # print(merge_sort(arrays))  # 输出：[1, 2, 3, 4, 5, 7, 8, 9, 10]
