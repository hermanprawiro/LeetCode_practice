class Solution:
    DIRECTIONS = (
        (0, 1), # right
        (1, 0), # down
        (0, -1), # left
        (-1, 0) # up
    )
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: # impossible
            return -1
        m, n = len(grid), len(grid[0])
        visited = set()
        queue = [(grid[0][0], 0, 0)]
        def _isValid(i: int, j: int) -> bool:
            return 0 <= i < m and 0 <= j < n and (i, j) not in visited

        while queue:
            t, i, j = heapq.heappop(queue)
            if i == m-1 and j == n-1:
                return t
            if not _isValid(i, j):
                continue
            visited.add((i, j))

            for dy, dx in self.DIRECTIONS:
                next_i = i + dy
                next_j = j + dx
                if _isValid(next_i, next_j):
                    # If difference between current time and required time to visit next cell
                    # is even, there would be additional wait time of 1, else 0
                    # Ex: in case 1, during t = 3, next req time is 5, we go back and forth
                    # spending 2 secs, so when we arrive at next cell, t = 6, (from 5 + 1).
                    # Suppose the same case but current time is t = 2, we can arrive at next
                    # cell at t = 5.
                    wait_time = 1 if ((grid[next_i][next_j] - t) % 2 == 0) else 0
                    next_t = max(t + 1, grid[next_i][next_j] + wait_time)
                    heapq.heappush(queue, (next_t, next_i, next_j))
        return -1