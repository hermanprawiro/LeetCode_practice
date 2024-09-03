class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # string manipulation approach
        # other approach is strictly use int and div + modulo

        # convert string to int
        # +1 because a = 1
        s = "".join([str(ord(x) - ord('a') + 1) for x in s])
        # do transformation k times
        result = 0
        for _ in range(k):
            result = sum([int(x) for x in s])
            s = str(result)
        return result
        