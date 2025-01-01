class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        m = sum(nums)
        if abs(target) > m:
            return 0
        # The most extreme possible sum values is m or -m (all + or all -)
        # so, target must be in [-m, m] range.
        # We only need to consider current and 1 previous index, so
        # instead of using 2d array, we can use 2 1d arrays.
        dp = [0] * (2 * m + 1) # [-m, ..., 0, ..., m]
        dp[m + nums[0]] += 1
        dp[m - nums[0]] += 1
        for i in range(1, n):
            new_dp = [0] * (2 * m + 1)
            for j in range(-m, m + 1):
                if dp[m + j] > 0:
                    new_dp[m + j + nums[i]] += dp[m + j]
                    new_dp[m + j - nums[i]] += dp[m + j]
            dp = new_dp
        # dp[0] is when sum = -m
        # dp[m] is when sum = 0
        # dp[2*m] is when sum = m
        return dp[m + target]