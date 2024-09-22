class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        while k:
            step = self.countSteps(n, cur, cur + 1)
            if step <= k:
                cur += 1
                k -= step
            else:
                cur *= 10
                k -= 1
        return cur

    def countSteps(self, n, a, b):
        steps = 0
        while a <= n:
            steps += min(n + 1, b) - a
            a *= 10
            b *= 10
        return steps