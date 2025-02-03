class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n_asc = 1
        n_desc = 1
        max_len = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                n_asc += 1
                n_desc = 1
            elif nums[i] > nums[i + 1]:
                n_desc += 1
                n_asc = 1
            else:
                n_asc = n_desc = 1
            max_len = max(max_len, n_asc, n_desc)
        return max_len