class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        answer = 0
        for i in range(1, n):
            j = n - i
            while stack and nums[stack[-1]] <= nums[j]:
                answer = max(answer, j - stack[-1])
                stack.pop()
        return answer