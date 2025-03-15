class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_r = 1
        max_r = max(nums)

        while min_r < max_r:
            mid_r = (max_r - min_r) // 2 + min_r
            n_theft = 0
            i = 0
            while i < n:
                if nums[i] <= mid_r:
                    n_theft += 1
                    i += 2 # skip adjacent
                else:
                    i += 1
            
            if n_theft >= k:
                max_r = mid_r
            else:
                min_r = mid_r + 1
        return min_r