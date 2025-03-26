class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # flatten grid then sort then select median
        answer = 0
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)
        n = len(nums)
        nums.sort()

        median = nums[n // 2]
        for num in nums:
            if num % x != median % x:
                return -1
            answer += abs(median - num) // x
        return answer

