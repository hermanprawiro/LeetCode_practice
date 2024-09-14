class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Maximum value of bitwise and of a subarray can be obtained
        if all the members of the subarray is the member with
        the maximum value in the original array.
        In other words, this problem is finding longest consecutive max elements.
        """
        max_value = 0
        current_streak = 0
        answer = 0
        for num in nums:
            if num > max_value:
                max_value = num
                current_streak = 1
                answer = max(answer, current_streak)
            elif num == max_value:
                current_streak += 1
                answer = max(answer, current_streak)
            else:
                current_streak = 0
        return answer