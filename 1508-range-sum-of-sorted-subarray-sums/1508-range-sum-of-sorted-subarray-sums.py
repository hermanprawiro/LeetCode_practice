class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sum = []
        # Calculating sum of subarrays
        for i in range(len(nums)):
            sum_ = 0
            for j in range(i, len(nums)):
                sum_ += nums[j]
                subarray_sum.append(sum_)
        subarray_sum.sort()
        
        # Return the result
        result = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            result = (result + subarray_sum[i]) % mod
        return result
        