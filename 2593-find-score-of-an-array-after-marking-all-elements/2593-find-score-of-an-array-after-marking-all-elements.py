class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        queue = []
        for i, num in enumerate(nums):
            heapq.heappush(queue, (num, i))
        score = 0
        marked = set()
        while queue:
            num, i = heapq.heappop(queue)
            if i in marked:
                continue
            score += num
            marked.add(max(0, i - 1))
            marked.add(min(n - 1, i + 1))
        return score
            