class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        servers = []
        enabled_rows = [0] * row
        enabled_cols = [0] * col
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    servers.append((i, j))
                    enabled_rows[i] += 1
                    enabled_cols[j] += 1
        answer = 0
        for (i, j) in servers:
            if enabled_rows[i] > 1 or enabled_cols[j] > 1:
                answer += 1
        return answer