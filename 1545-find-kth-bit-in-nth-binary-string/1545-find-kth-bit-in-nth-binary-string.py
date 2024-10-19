class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        n_str = 2 ** n # actually n**2 - 1
        # but it's more convenient to + 1 because k is 1-indexed
        # ex: n = 3, n_str = 7, str = "0111001"
        # first half => k < (n_str + 1) // 2, so it's k < 4 (1-indexed)
        # middle => k == (n_str + 1) // 2, k == 4 
        if k < n_str // 2:
            return self.findKthBit(n - 1, k)
        elif k == n_str // 2:
            return "1"
        else:
            val = self.findKthBit(n - 1, n_str - k)
            return "1" if val == "0" else "0"