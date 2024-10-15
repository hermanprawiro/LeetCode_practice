class Solution:
    def minimumSteps(self, s: str) -> int:
        n_black = 0
        answer = 0
        for i in range(len(s)):
            if s[i] == "1":
                n_black += 1
            else:
                answer += n_black
        return answer
