class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        We can only use one loop and a hash map (dict in python).
        For each element in nums, we look for the complement (target - current_num)
        in the dict. If it found, return the indices, else store the current_num
        to the dict.
        """
        complements = {}
        for k, v in enumerate(nums):
            complement = target - v
            if complement in complements.keys():
                return [k, complements[complement]]
            complements[v] = k