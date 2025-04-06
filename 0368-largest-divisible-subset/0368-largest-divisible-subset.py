class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n # dp[i] is length of the longest subset that ends at index i
        prev = [-1] * n # prev[i] is the index of the previous element in the longest subset
        max_i = 0 # because the answer is not always at dp[-1]

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                if dp[i] > dp[max_i]:
                    max_i = i
        
        result = []
        i = max_i
        while i >= 0:
            result.append(nums[i])
            i = prev[i]
        return result
