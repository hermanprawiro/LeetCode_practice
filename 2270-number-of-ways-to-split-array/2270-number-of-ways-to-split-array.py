class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        # Originally, this can be solved using a prefix array, space comp O(n).
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

        # If we look at the second loop, the prefix[-1] is constant, and
        # the prefix[i] can be calculated in the second loop.
        # So, we can improve this to only use 2 int, left_sum and right_sum.
        # Time comp is the same, space comp become O(1).
        """
        left_sum = 0
        right_sum = sum(nums)
        answer = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum >= (right_sum - left_sum):
                answer += 1
        return answer

        return answer