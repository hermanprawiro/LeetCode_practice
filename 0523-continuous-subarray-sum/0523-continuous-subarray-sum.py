class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # brute force with two pointers is too slow
        # so we need to use only one loop with cumsum
        
        # loop and calculate the cumulative sum up to this point
        # store the remainder (cumsum % k) to dict with its idx
        # in the future, if we encounter the same remainder before, 
        # by substracting current cumsum with the past cumsum
        # we can get to remainder == 0 (target)
        # we just need to ensure current_idx - past_idx >= subarray_length (2)
        dict_remainder = {0: -1}
        cumsum = 0

        for i in range(len(nums)):
            num = nums[i]
            cumsum += num
            remainder = cumsum % k
            if remainder in dict_remainder:
                if i - dict_remainder[remainder] >= 2:
                    return True
            else:
                dict_remainder[remainder] = i
        return False