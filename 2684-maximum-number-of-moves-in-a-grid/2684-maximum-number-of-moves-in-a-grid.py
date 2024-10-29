class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0] * col for _ in range(row)]
        for i in range(row):
            dp[i][0] = 1 # init first column
        answer = 0

        for j in range(1, col):
            for i in range(row):
                # same row
                if grid[i][j] > grid[i][j - 1] and dp[i][j - 1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i][j - 1])
                # down right
                if i - 1 >= 0 and grid[i][j] > grid[i - 1][j - 1] and dp[i - 1][j - 1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j - 1])
                # up right
                if i + 1 < row and grid[i][j] > grid[i + 1][j - 1] and dp[i + 1][j - 1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i + 1][j - 1])
                answer = max(answer, dp[i][j] - 1) # because first col doesn't count
        return answer