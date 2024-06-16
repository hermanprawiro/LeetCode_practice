class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        n_patch = 0
        missing = 1
        i = 0

        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                n_patch += 1
        return n_patch