class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # calculate prefix XOR for each number
        # n is the length of array nums
        # target is (2**maximumBit) - 1
        # so answer is prefix[i] XOR target
        # reverse the answer because query 0 is (pre[n - 1] XOR target) and query (n - 1) is (pre[0] XOR target)
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] ^ nums[i]
        target = 2**maximumBit - 1
        return [pre[i] ^ target for i in range(n - 1, -1, -1)]