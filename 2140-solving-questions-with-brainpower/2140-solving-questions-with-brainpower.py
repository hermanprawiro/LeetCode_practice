class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        answer = 0
        n = len(questions)
        # init dp array with length (n + 1), so dp[n] = 0 to handle out of bound index
        # using dp[min(n, idx)]
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            point = questions[i][0]
            brainpower = questions[i][1]

            # solve
            next_solve_idx = i + brainpower + 1
            point_solve = point + dp[min(n, next_solve_idx)]

            # skip
            point_skip = dp[min(n, i + 1)]

            dp[i] = max(point_solve, point_skip)

        return dp[0]
