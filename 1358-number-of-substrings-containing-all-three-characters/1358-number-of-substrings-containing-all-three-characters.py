class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_idx = [-1] * 3
        answer = 0
        for i in range(len(s)):
            last_idx[ord(s[i]) - ord('a')] = i

            # If there's still any char we haven't encountered, the min(last_idx) = -1,
            # which means we add 0 to the answer.
            answer += 1 + min(last_idx)
        return answer