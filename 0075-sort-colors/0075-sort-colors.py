class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict_count = {}
        for num in nums:
            if num in dict_count:
                dict_count[num] += 1
            else:
                dict_count[num] = 1
        
        prev = 0
        for i in range(3):
            if i not in dict_count:
                continue
            count = dict_count[i]
            for j in range(count):
                nums[prev + j] = i
            prev += count
        