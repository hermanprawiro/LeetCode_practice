class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # for prefix sum
        counts = [0] * (n + 1)
        counts[0] = 1 # default

        result = 0
        n_odd = 0

        for num in nums:
            if num % 2:
                n_odd += 1
            if n_odd - k >= 0:
                result += counts[n_odd - k]
            counts[n_odd] += 1
        return result