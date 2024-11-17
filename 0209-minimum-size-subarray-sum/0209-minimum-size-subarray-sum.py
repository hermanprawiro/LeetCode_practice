class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        answer = len(nums)
        sums = 0
        for right in range(len(nums)):
            sums += nums[right]
            while sums >= target and left <= right:
                answer = min(answer, right - left + 1)
                sums -= nums[left]
                left += 1
        return answer if answer != len(nums) else 0