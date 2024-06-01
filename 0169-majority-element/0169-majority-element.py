class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_nums = {}
        n = len(nums)
        if n == 1:
            return nums[0]

        for num in nums:
            if num in dict_nums.keys():
                current_count = dict_nums[num] + 1
                if current_count > (n // 2):
                    return num
                else:
                    dict_nums[num] = current_count
            else:
                dict_nums[num] = 1
        