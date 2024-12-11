class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # subsequence is not necessarily need to be contiguous
        # that's substring
        
        # edge case when len(nums) == 1
        if len(nums) == 1:
            return 1

        maxval = max(nums)
        count = [0] * (maxval + 1)
        for num in nums:
            # range start
            count[max(0, num - k)] += 1 # cap at index 0
            # range end, +1 because inclusive
            if num + k + 1 <= maxval: # only if inside [0, maxval] range
                count[num + k + 1] -= 1
        answer = 0
        cursum = 0
        for val in count:
            cursum += val
            answer = max(answer, cursum)
        return answer