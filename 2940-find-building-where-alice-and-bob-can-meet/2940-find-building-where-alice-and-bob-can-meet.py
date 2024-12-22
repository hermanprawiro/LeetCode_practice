class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answer = [-1] * len(queries)
        new_queries = [[] for _ in range(len(heights))]

        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if heights[a] < heights[b] or a == b:
                answer[i] = b
            else:
                new_queries[b].append((max(heights[a], heights[b]), i))
        
        queue = [] # min heap
        for i, height in enumerate(heights):
            while queue and queue[0][0] < height:
                _, q_idx = heapq.heappop(queue)
                answer[q_idx] = i
            for elem in new_queries[i]:
                heapq.heappush(queue, elem)
        return answer