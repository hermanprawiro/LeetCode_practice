class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # possible char is lowercase a, b, c
        # instead of use two windows from start and end, we use 1 window
        # in the middle to maximize untaken chars which equals to minimize
        # those two windows as long as (total_count - count_window) >= k
        n = len(s)
        counts = [0] * 3 # total count
        for char in s:
            counts[ord(char) - ord('a')] += 1
        if min(counts) < k: # edge case
            return -1
        # start sliding window
        left = max_window_length = 0
        in_window = [0] * 3
        for right in range(n):
            in_window[ord(s[right]) - ord('a')] += 1
            while left <= right and any([counts[i] - in_window[i] < k for i in range(3)]):
                in_window[ord(s[left]) - ord('a')] -= 1
                left += 1
            max_window_length = max(max_window_length, right - left + 1)
        return n - max_window_length
        