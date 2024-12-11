class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        answer = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            count[c] = count.get(c, 0) + 1
            max_count = max(max_count, count[c])
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer



