class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        answer = 0
        sets = set(nums)

        for num in nums:
            cur_streak = 0
            cur_num = num
            while cur_num in sets and cur_num <= 10**5:
                cur_streak += 1
                cur_num = cur_num * cur_num
            answer = max(answer, cur_streak)
        return answer if answer > 1 else -1
        