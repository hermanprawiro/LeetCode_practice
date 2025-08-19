class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        max_streak = 0
        for num in nums:
            if num == 0:
                max_streak += 1
                answer += max_streak
            else:
                max_streak = 0
        return answer
