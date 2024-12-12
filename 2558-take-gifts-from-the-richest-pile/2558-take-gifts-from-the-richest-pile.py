class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        queue = []
        # default is minheap, add - to turn into maxheap
        for gift in gifts:
            heapq.heappush(queue, -gift)
        # simulate
        for i in range(k):
            val = -heapq.heappop(queue)
            val = int(val ** 0.5)
            heapq.heappush(queue, -val)
        return -sum(queue) # don't forget to turn back into +