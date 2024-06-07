class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        l = 0
        for r in range(1, n):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1