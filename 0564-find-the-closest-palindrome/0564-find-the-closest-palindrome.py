class Solution:
    def nearestPalindromic(self, n: str) -> str:
        sz = len(n)
        if sz == 1:
            val = int(n)
            if val == 0:
                return "1"
            return str(val - 1)
        
        return n[:sz//2 + (sz % 2)] + n[:sz//2][::-1]