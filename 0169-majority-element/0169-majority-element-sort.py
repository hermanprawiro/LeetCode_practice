class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        return nums[n // 2]
        