class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * (n - k + 1)
        streak = 1
        for i in range(n - 1):
            if nums[i + 1] == (nums[i] + 1):
                streak += 1
            else:
                streak = 1
            if streak >= k:
                result[i - k + 2] = nums[i + 1]
        return result
