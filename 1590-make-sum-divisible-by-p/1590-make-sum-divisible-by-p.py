class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target = total_sum % p
        if target == 0:
            return 0
        
        mods = {0: -1}
        sum_mod = 0
        min_len = n = len(nums)
        
        for i in range(n):
            sum_mod = (sum_mod + nums[i]) % p
            needed = (sum_mod - target + p) % p
            if needed in mods:
                min_len = min(min_len, i - mods[needed])
            mods[sum_mod] = i
        return -1 if min_len == n else min_len