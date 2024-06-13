class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        elems = set()
        for val in nums:
            try:
                elems.remove(val)
            except:
                elems.add(val)
        return elems.pop()