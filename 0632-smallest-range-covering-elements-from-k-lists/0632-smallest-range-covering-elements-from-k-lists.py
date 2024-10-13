class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        heap = []

        ans_start = 0
        ans_end = float('inf')
        val_max = float('-inf')
        # insert the first value from each list while tracking the max val
        # we can always obtain min val from the heap
        for i in range(n):
            heapq.heappush(heap, (nums[i][0], i, 0)) # (val, rows, cols)
            val_max = max(val_max, nums[i][0])
        
        # now the heap contains n numbers
        # we replace the min val with the next number from the same inner list
        # (same row, i + 1 column), when it doesn't exist, end the loop
        while len(heap) == n:
            val_min, row, col = heapq.heappop(heap)
            # because we start from small index, just ignore if range is equal
            if val_max - val_min < ans_end - ans_start:
                ans_start = val_min
                ans_end = val_max
            
            if col + 1 < len(nums[row]):
                heapq.heappush(heap, (nums[row][col + 1], row, col + 1))
                val_max = max(val_max, nums[row][col + 1])
        
        return [ans_start, ans_end]