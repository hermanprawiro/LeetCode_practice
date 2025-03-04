class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self._helper(0, n)
    
    def _helper(self, power: int, n: int) -> bool:
        if n == 0:
            return True
        
        if 3**power > n:
            return False

        is_add = self._helper(power + 1, n - 3**power)
        is_skip = self._helper(power + 1, n)
        return is_add or is_skip