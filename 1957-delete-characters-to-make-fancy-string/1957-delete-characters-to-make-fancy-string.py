class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        ss = list(s)
        # because max 3 consecutive chars, we just start from the 3rd char
        i = 2 # write pointer
        # j is read pointer
        for j in range(i, len(s)):
            if ss[j] != ss[i - 1] or ss[j] != ss[i - 2]:
                ss[i] = ss[j]
                i += 1
        return "".join(ss[:i])
