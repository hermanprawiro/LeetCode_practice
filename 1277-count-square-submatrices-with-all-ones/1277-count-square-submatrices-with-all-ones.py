class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Bottom up DP
        We iteratively check 2x2 submatrix
        Whenever the bottom right is 1, check the top, left, and top left cell
        Take the min value then +1 (the bottom right itself)
        So, we initialize dp matrix with row + 1 and col + 1
        """
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        answer = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                    answer += dp[i + 1][j + 1]
        return answer