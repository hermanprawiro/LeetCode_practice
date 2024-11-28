class Solution:
    DIRECTIONS = (
        (0, 1), # right
        (-1, 0), # down
        (0, -1), # left
        (1, 0) # up
    )
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # helper to check index is inside grid
        def _isValid(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n
        min_obstacles = [[float('inf')] * n for _ in range(m)]
        min_obstacles[0][0] = 0
        
        # Dijkstra + Heap (TLE)
        # queue = []
        # queue.append((0, 0, 0)) # (row, col, n_obstacles)
        # while queue:
        #     i, j, n_obstacles = heapq.heappop(queue)
        #     if i == m-1 and j == n-1: # reached target
        #         return n_obstacles
        #     for dir_i, dir_j in self.DIRECTIONS:
        #         new_i, new_j = i + dir_i, j + dir_j
        #         if _isValid(new_i, new_j):
        #             new_n = n_obstacles + grid[new_i][new_j]
        #             if new_n < min_obstacles[new_i][new_j]: # found better path
        #                 min_obstacles[new_i][new_j] = new_n
        #                 heapq.heappush(queue, (new_i, new_j, new_n))
        # return min_obstacles[m-1][n-1]

        # 0-1 BFS
        queue = deque([(0, 0, 0)]) # (row, col, n_obstacles)
        while queue:
            i, j, n_obstacles = queue.popleft()
            for dir_i, dir_j in self.DIRECTIONS:
                new_i, new_j = i + dir_i, j + dir_j
                if _isValid(new_i, new_j) and min_obstacles[new_i][new_j] == float('inf'):
                    if grid[new_i][new_j] == 1: # if obstacle, count + 1 and add to back of queue
                        min_obstacles[new_i][new_j] = n_obstacles + 1
                        queue.append((new_i, new_j, n_obstacles + 1))
                    else: # if empty, keep the cound and add to front of queue
                        min_obstacles[new_i][new_j] = n_obstacles
                        queue.appendleft((new_i, new_j, n_obstacles))
        return min_obstacles[m-1][n-1]
