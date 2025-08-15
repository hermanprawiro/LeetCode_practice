class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Condition:
        1.  Power of four must be a positive number.
        2.  If n is a power of four, n is also a power of two.
            Power of two has only one '1' bit in its binary representation.
            To quickly check this property, we can use:
            (n & (n - 1)) == 0
            Example: suppose n = 8.
            8 --> 0 1 0 0 0
            7 --> 0 0 1 1 1
            & --> 0 0 0 0 0    0 == 0
            Example: suppose n = 7.
            7 --> 0 0 1 1 1
            6 --> 0 0 1 1 0
            & --> 0 0 1 1 0    6 != 0
        3.  Power of four has one '1' bit in even position.
            To quickly check this property, we can use:
            (n - 1) % 3 == 0
            This is because n = 4**x can be written as n = (3 + 1)**x = 3**x + 1.
            So, (n - 1) should be divisible by 3.
        """
        if n <= 0:
            return False

        if not (n & (n - 1)) == 0:
            return False

        return (n - 1) % 3 == 0