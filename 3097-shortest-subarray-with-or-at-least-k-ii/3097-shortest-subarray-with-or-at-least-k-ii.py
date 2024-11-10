class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        answer = float('inf')
        start = end = 0
        bits = [0] * 32
        while end < len(nums):
            self._updateBits(bits, nums[end], 1)
            while start <= end and self._bitToInt(bits) >= k:
                answer = min(answer, end - start)
                self._updateBits(bits, nums[start], -1)
                start += 1
            end += 1
        return -1 if answer == float('inf') else answer

    def _updateBits(self, bits: List[int], num: int, sign: int):
        for pos in range(len(bits)):
            if num & (1 << pos):
                bits[pos] += sign
    
    def _bitToInt(self, bits: List[int]) -> int:
        result = 0
        for pos in range(len(bits)):
            result |= 1 << pos if bits[pos] else 0
        return result
