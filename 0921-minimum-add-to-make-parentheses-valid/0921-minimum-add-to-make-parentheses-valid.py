class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n_open = 0 # num of found opening bracket
        n_close = 0 # num of MISSING closing bracket

        for char in s:
            if char == "(":
                n_open += 1
            else:
                if n_open:
                    n_open -= 1
                else:
                    n_close += 1
        return n_open + n_close