class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Array is sorted in ascending order, then rotated.
        There must be <= 1 instances where nums[i] > nums[i + 1], else invalid.
        Case when 0 is when the array contains only one value.
        """
        n = len(nums)
        n_desc = 1 if nums[n - 1] > nums[0] else 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                n_desc += 1
        return n_desc <= 1