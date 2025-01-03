class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prev = 0
        for i in range(n):
            prev += nums[i]
            prefix[i] = prev

        answer = 0
        for i in range(n - 1):
            left = prefix[i]
            right = prefix[-1] - prefix[i]
            if left >= right:
                answer += 1
        return answer