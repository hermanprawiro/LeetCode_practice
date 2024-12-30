class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # how many good strings of length i in range [0, high]
        # dp[0] = 1 (only empty strings)
        dp = [1] + [0] * high
        modulo = 10**9 + 7

        for n in range(1, high + 1):
            if n >= zero:
                dp[n] += dp[n - zero]
            if n >= one:
                dp[n] += dp[n - one]
            dp[n] %= modulo
        
        return sum(dp[low:high+1]) % modulo