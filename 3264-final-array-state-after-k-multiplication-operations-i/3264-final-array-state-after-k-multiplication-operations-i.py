class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        queue = []
        for i, num in enumerate(nums):
            heapq.heappush(queue, (num, i))
        for j in range(k):
            num, i = heapq.heappop(queue)
            nums[i] *= multiplier
            heapq.heappush(queue, (nums[i], i))
        return nums