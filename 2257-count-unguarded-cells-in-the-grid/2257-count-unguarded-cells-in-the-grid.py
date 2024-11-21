class Solution:
    UNGUARDED = 0
    WALL = 1
    GUARD = 2
    GUARDED = 3
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]
        for wall in walls:
            grid[wall[0]][wall[1]] = self.WALL
        for guard in guards:
            grid[guard[0]][guard[1]] = self.GUARD

        for guard in guards:
            y, x = guard
            # up
            for i in range(y - 1, -1, -1):
                if grid[i][x] == self.GUARD or grid[i][x] == self.WALL:
                    break
                grid[i][x] = self.GUARDED
            # down
            for i in range(y + 1, m):
                if grid[i][x] == self.GUARD or grid[i][x] == self.WALL:
                    break
                grid[i][x] = self.GUARDED
            # left
            for i in range(x - 1, -1, -1):
                if grid[y][i] == self.GUARD or grid[y][i] == self.WALL:
                    break
                grid[y][i] = self.GUARDED
            for i in range(x + 1, n):
                if grid[y][i] == self.GUARD or grid[y][i] == self.WALL:
                    break
                grid[y][i] = self.GUARDED

        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.UNGUARDED:
                    answer += 1
        return answer