class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        self.memo = {}
        self.n = n

        return 1 + self.findMinSteps(1, 1)

    def findMinSteps(self, n_current, n_clipboard) -> int:
        if n_current == self.n:
            return 0
        elif n_current > self.n:
            return float('inf')
        elif (n_current, n_clipboard) in self.memo:
            return self.memo[(n_current, n_clipboard)]

        # copy and paste
        n_copypaste = 2 + self.findMinSteps(n_current * 2, n_current)

        # only paste
        n_paste = 1 + self.findMinSteps(n_current + n_clipboard, n_clipboard)

        self.memo[(n_current, n_clipboard)] = min(n_copypaste, n_paste)
        return self.memo[(n_current, n_clipboard)]
    