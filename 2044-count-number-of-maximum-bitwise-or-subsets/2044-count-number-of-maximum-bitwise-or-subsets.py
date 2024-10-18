class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        # first find the maximum possible or value
        for num in nums:
            max_or |= num
        return self.countSubsets(nums, 0, 0, max_or)

    def countSubsets(self, nums: List[int], idx: int, current_or: int, target_or: int) -> int:
        if idx == len(nums):
            return 1 if current_or == target_or else 0

        count_without = self.countSubsets(nums, idx + 1, current_or, target_or)
        count_with = self.countSubsets(nums, idx + 1, current_or | nums[idx], target_or)
        return count_without + count_with