class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        mismatch = 0
        diff1 = 0
        diff2 = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch += 1
                if mismatch > 2:
                    return False
                elif mismatch == 1:
                    diff1 = i
                else:
                    diff2 = i

        return s1[diff1] == s2[diff2] and s1[diff2] == s2[diff1]