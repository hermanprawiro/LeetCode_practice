class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # max element in nums is 10^7 ~ 16 * 1024 * 1024 ~ 2^24 ~ 24 bits
        # count bitwise and of every candidate in each bit position
        # then return the max
        max_count = 0
        for i in range(24):
            cur_count = 0
            for num in candidates:
                cur_count += (num & (1 << i) > 0)
            max_count = max(max_count, cur_count)
        return max_count
