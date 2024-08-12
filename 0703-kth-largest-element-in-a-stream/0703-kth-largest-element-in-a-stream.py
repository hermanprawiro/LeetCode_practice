class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # construct a heap that contains only k largest element
        # in python, the default heap is min-heap
        # so, the first element of the heap will be the kth element
        self.k = k
        self.heap = nums[:]
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)