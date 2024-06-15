class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort(key=lambda x: x[0]) # sort ascending by cost

        max_heap = []
        i = 0
        for _ in range(k):
            # push projects that fit the budget
            while i < n and projects[i][0] <= w:
                # by default, heap in python is min heap
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            # if no project fits the budget
            if not max_heap:
                break
            # the profits in heap is negative
            w -= heapq.heappop(max_heap)
        return w
        