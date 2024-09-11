class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0
        """
               int   binary
        start = 10 => 1010
        goal  =  7 => 0111
        xor   = 13 => 1101
        """
        xor = start ^ goal

        # to count the different bits, we can use 2 approaches
        # 1. bit shift and bitwise and (&)
        # while xor:
        #     result += xor & 1 # evaluate rightmost bit and 1
        #     xor >>= 1

        # 2. convert to string and count 1s
        # bin(13) => '0b1101'
        result = bin(xor).count('1')
        return result
