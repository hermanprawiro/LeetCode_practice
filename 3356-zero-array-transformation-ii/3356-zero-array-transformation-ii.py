class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        diffs = [0] * (n + 1)
        k = 0
        presum = 0

        for i in range(n): # iterate through nums
            while presum + diffs[i] < nums[i]: # iterate through queries
                k += 1
                if k > len(queries):
                    return -1
                
                left, right, val = queries[k - 1]
                # we only interested in the query that covers current i
                if right >= i:
                    diffs[max(left, i)] += val
                    diffs[right + 1] -= val

            presum += diffs[i]
        return k
            