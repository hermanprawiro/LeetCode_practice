class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for i in range(len(str1)):
            if j == len(str2):
                return True
            c1 = str1[i]
            c2 = str2[j]
            if c1 == c2:
                j += 1
            elif ord(c2) - ord(c1) == 1 or ord(c2) - ord(c1) == -25:
                j += 1
        return j == len(str2)