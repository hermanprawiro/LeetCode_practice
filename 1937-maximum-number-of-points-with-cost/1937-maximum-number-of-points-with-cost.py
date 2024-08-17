class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        row = len(points)
        col = len(points[0])

        dp = points[0] # we are free to choose cells in the first row
        left = [0] * col
        right = [0] * col

        for r in range(1, row):
            for c in range(col):
                if c == 0:
                    left[c] = dp[c]
                else:
                    left[c] = max(left[c - 1] - 1, dp[c])
            
            for c in range(col - 1, -1, -1):
                if c == col - 1:
                    right[c] = dp[c]
                else:
                    right[c] = max(right[c + 1] - 1, dp[c])
            
            for c in range(col):
                dp[c] = points[r][c] + max(left[c], right[c])
        
        return max(dp)