class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)

        flip_start = [0] * n # track where do we need to start flipping
        flip_count = 0 # track how many flips
        is_flip = 0 # track are we currently in an active flip window

        for i in range(n):
            # end the currently active flip
            if i >= k:
                is_flip ^= flip_start[i - k] # XOR operator to toggle
            
            # check whether we need to flip current number
            if is_flip == nums[i]:
                # if we need to flip but the end of the flip window
                # exceed the length of array, then it's impossible
                if i + k > n:
                    return -1
                flip_start[i] = 1
                flip_count += 1
                is_flip ^= 1 # XOR operator to toggle
        
        return flip_count
        