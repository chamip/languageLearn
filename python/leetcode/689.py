class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        ans = []
        sum1, maxSum1, maxSum1Idx = 0, 0, 0
        sum2, maxSum12, maxSum12Idx = 0, 0, 0
        sum3, maxTotal, maxSum123Idx = 0, 0, 0
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > maxSum1:
                    maxSum1 = sum1
                    maxSum1Idx = i - k * 3 + 1
                    print(maxSum1Idx, end='a')
                if maxSum1 + sum2 > maxSum12:
                    maxSum12 = maxSum1 + sum2
                    maxSum12Idx = i - k * 2 + 1
                    print(maxSum12Idx, end='b')
                if maxSum12 + sum3 > maxTotal:
                    maxTotal = maxSum12 + sum3
                    maxSum123Idx = i - k + 1
                    #ans = [maxSum1Idx, maxSum12Idx, i - k + 1]
                    print(maxSum123Idx, end='/')
                    print()
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        ans = [maxSum1Idx, maxSum12Idx, maxSum123Idx]
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))

