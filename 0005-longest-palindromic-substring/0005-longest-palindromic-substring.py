class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(left: int, right: int) -> bool:
            # [left, right)
            i = left
            j = right - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for n in range(len(s), 0, -1):
            for start in range(len(s) - n + 1):
                if isPalindrome(start, start + n):
                    return s[start:start+n]
        return ""