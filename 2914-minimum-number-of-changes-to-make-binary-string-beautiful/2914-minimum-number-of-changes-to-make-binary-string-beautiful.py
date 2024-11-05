class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        answer = 0
        for i in range(n // 2):
            if s[i * 2] != s[i * 2 + 1]:
                answer += 1
        return answer