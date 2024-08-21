class Solution:
    def strangePrinter(self, s: str) -> int:
        # Top-down DP with memo
        memo = {}
        # Remove duplicate chars
        s = "".join([k for k, g in itertools.groupby(s)])
        n = len(s)

        def minTurns(start: int, end: int) -> int:
            if start > end:
                return 0
            if (start, end) in memo:
                return memo[(start, end)]
            # initialize with worst case: no matching chars
            result = 1 + minTurns(start + 1, end)
            # try to optimize
            for i in range(start + 1, end + 1):
                if s[i] == s[start]:
                    result_with_match = minTurns(start, i - 1) + minTurns(i + 1, end)
                    result = min(result, result_with_match)
            memo[(start, end)] = result
            return result

        return minTurns(0, n - 1)