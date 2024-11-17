class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * (n - k + 1)
        for i in range(n - k + 1):
            is_valid = True
            for j in range(k - 1):
                if nums[i + j + 1] != nums[i + j] + 1:
                    is_valid = False
            if is_valid:
                result[i] = nums[i + k - 1]
        return result

