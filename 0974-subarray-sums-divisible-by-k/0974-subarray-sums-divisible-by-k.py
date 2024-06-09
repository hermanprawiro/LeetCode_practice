class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        
        dict_remainder = {0: 1}
        cumsum = 0

        for i in range(len(nums)):
            num = nums[i]
            cumsum += num
            remainder = cumsum % k
            if remainder < 0:
                remainder += k
            if remainder in dict_remainder:
                result += dict_remainder[remainder]
                dict_remainder[remainder] += 1
            else:
                dict_remainder[remainder] = 1
        return result