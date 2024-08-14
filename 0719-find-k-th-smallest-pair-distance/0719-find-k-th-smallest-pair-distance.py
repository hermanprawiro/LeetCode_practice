class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # use binary search and two pointers
        n = len(nums)
        nums.sort()
        low = 0 # because the distance is absolute distance
        high = nums[-1] - nums[0]

        while low < high:
            mid = low + (high - low) // 2
            if self.countPairs(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

    def countPairs(self, nums: List[int], max_dist: int) -> int:
        count = 0
        j = 1
        n = len(nums)
        for i in range(n):
            # move the second pointer forward until the distance is >= max_dist
            while j < n and nums[j] - nums[i] <= max_dist:
                j += 1
            count += j - i - 1
        return count
