class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_m = sum(rolls)
        sum_mn = mean * (m + n)
        sum_n = sum_mn - sum_m
        # sum of remaining must be (n <= sum_n <= 6n)
        if sum_n > (6 * n) or sum_n < n:
            return []
        # each dice roll should be close to its mean
        # then distribute the modulo
        mean_n = sum_n // n
        mod_n = sum_n % n
        result = [mean_n] * n
        for i in range(mod_n):
            result[i] += 1
        return result