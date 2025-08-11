class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Instead of using the powers as is, we store the exponent instead.
        Then we calculate the prefix sum of the exponents.
        """
        mod = 10**9 + 7

        bins = []
        cur = 0
        while n > 0:
            if n % 2 == 1:
                bins.append(cur)
            n //= 2
            cur += 1
        
        presum = [0] * len(bins)
        presum[0] = bins[0]
        for i in range(1, len(bins)):
            presum[i] = presum[i - 1] + bins[i]
        
        answer = []
        for left, right in queries:
            if left == right:
                cur = 2 ** bins[right] % mod
            else:
                cur = 2 ** (presum[right] - presum[left]) % mod
            answer.append(cur)
        
        return answer
