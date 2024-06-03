class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s) // 2
        return s[:n] == s[::-1][:n]