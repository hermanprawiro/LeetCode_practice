class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        answer = 0
        left = 0
        for right in range(len(s)):
            c = s[right] # new char
            count[c] = count.get(c, 0) + 1 # get count of new char
            max_count = max(max_count, count[c]) # count of dominant char
            # the window_size - count of dominant char in the window = count replaceable char
            # if the replaceable char > k, we reached the current max window size
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer



