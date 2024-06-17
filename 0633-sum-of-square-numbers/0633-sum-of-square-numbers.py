class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            cur_sum = left * left + right * right
            if cur_sum == c:
                return True
            elif cur_sum < c:
                left += 1
            else:
                right -= 1
        return False