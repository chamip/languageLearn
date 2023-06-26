from typing import List


class Solution:

    # def __init__(self, nums, firstLen, secondLen):
    #     self.nums = nums
    #     self.firstLen = firstLen
    #     self.secondLen = secondLen

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """两个非重叠子数组的最大和"""
        return max(self.solve(nums, firstLen, secondLen), self.solve(nums, secondLen, firstLen))

    def solve(self, nums, firstLen, secondLen):
        suml, sumr, maxsuml, res = 0, 0, 0, 0
        suml = sum(nums[x] for x in range(firstLen))
        sumr = sum(nums[x] for x in range(firstLen, firstLen + secondLen))
        maxsuml = suml
        res = suml + sumr
        j = firstLen
        for i in range(firstLen + secondLen, len(nums)):
            suml += nums[j] - nums[j - firstLen]
            maxsuml = max(maxsuml, suml)
            sumr += nums[i] - nums[i - secondLen]
            res = max(res, maxsuml + sumr)
            j += 1
        return res


if __name__ == '__main__':
    l = [1, 0, 3]
    firstLen = 1
    secondLen = 2
    s = Solution()
    ans = s.maxSumTwoNoOverlap(l, firstLen, secondLen)
    print(ans)
