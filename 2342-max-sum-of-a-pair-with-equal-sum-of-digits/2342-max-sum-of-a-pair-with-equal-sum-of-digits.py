class Solution:
    def calcDigitSum(self, num: int) -> int:
        digit_sum = 0
        while num:
            num, remainder = divmod(num, 10)
            digit_sum += remainder
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        """
        Max nums[i] = 10e9, which means the max digit sums comes from
        999999999 = 9*9 = 81.
        """
        sum_map = [0] * 82
        answer = -1
        
        for num in nums:
            digit_sum = self.calcDigitSum(num)
            if sum_map[digit_sum] > 0: # only if there's another num with the same digit sum
                answer = max(answer, sum_map[digit_sum] + num)
            sum_map[digit_sum] = max(sum_map[digit_sum], num)
        return answer