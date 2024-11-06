class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # init with the first num, loop from the second num
        set_bit = self.countSetBit(nums[0])
        cur_min = cur_max = nums[0]
        prev_max = float('-inf')

        for i in range(1, len(nums)):
            cur = nums[i]
            if self.countSetBit(cur) == set_bit:
                cur_min = min(cur_min, cur)
                cur_max = max(cur_max, cur)
            else:
                if prev_max > cur_min:
                    return False
                prev_max = cur_max
                cur_min = cur_max = cur
                set_bit = self.countSetBit(cur)
        if prev_max > cur_min: # for last segment
            return False
        return True
        
    def countSetBit(self, num: int) -> int:
        return bin(num).count('1')