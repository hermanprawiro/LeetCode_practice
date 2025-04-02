class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # maximize (nums[i] - nums[j]) * nums[k] means
        # first part is maximized when nums[i] is maximized and nums[j] is minimized
        answer = 0
        max_i = 0
        max_ij = 0
        for k in range(len(nums)):
            answer = max(answer, max_ij * nums[k])
            max_ij = max(max_ij, max_i - nums[k])
            max_i = max(max_i, nums[k])
        return answer