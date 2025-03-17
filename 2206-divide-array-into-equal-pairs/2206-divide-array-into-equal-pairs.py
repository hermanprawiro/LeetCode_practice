class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        for num, count in freqs.items():
            if count % 2 == 1:
                return False
        return True