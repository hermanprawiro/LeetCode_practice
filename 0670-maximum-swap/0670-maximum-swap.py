class Solution:
    def maximumSwap(self, num: int) -> int:
        numstr = list(str(num))
        n = len(numstr)
        max_right_idx = [0] * n
        max_right_idx[n - 1] = n - 1
        for i in range(2, n + 1):
            if numstr[-i] > numstr[max_right_idx[-i + 1]]:
                max_right_idx[-i] = n - i
            else:
                max_right_idx[-i] = max_right_idx[-i + 1]
        for i in range(n):
            if numstr[i] < numstr[max_right_idx[i]]:
                numstr[i], numstr[max_right_idx[i]] = numstr[max_right_idx[i]], numstr[i]
                return int("".join(numstr))
        return num