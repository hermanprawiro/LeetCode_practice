class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [0] * len(s)
        prefix[0] = int(s[0])
        for i in range(1, len(s)):
            prefix[i] = prefix[i - 1] + int(s[i])
        
        answer = 0
        for i in range(1, len(s)):
            left = i - prefix[i - 1]
            right = prefix[-1] - prefix[i - 1]
            answer = max(answer, left + right)
        return answer