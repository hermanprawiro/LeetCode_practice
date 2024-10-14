class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        answer = 0
        for _ in range(k):
            val = -heapq.heappop(heap)
            answer += val
            val = ceil(val / 3)
            heapq.heappush(heap, -val)
        return answer