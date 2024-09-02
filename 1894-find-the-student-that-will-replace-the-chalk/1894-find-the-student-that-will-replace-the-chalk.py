class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        psum = [0] * n
        prev = 0
        for i in range(n):
            cur = chalk[i]
            psum[i] = prev + cur
            prev = psum[i]
            if prev > k:
                return i
        
        k = k % psum[-1]
        is_replace = False
        i = 0
        while not is_replace:
            cur = chalk[i]
            if k < cur:
                return i
            k -= cur
            i += 1
            if i == n:
                i = 0
        return 0