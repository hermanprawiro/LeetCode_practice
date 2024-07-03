class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # if the array contains <= 4 numbers, we can
        # make all of them equal so the diff = 0
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        result = nums[-1] - nums[0] # max diff if we remove nothing
        # we need to calculate diff between idx: 
        # 0 and -4 | smallest and 4th largest (if we remove all largest 3)
        # 1 and -3 | 2nd smallest and 3rd largest (if we remove smallest and largest 2)
        # ...
        # 3 and -1 | 4th smallest and largest (if we remove all smallest 3)
        for i in range(4):
            result = min(result, nums[-(4 - i)] - nums[i])
        return result