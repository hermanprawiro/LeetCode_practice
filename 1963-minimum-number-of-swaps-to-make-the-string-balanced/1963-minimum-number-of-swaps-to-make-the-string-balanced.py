class Solution:
    def minSwaps(self, s: str) -> int:
        opening, closing = 0, 0
        swaps = 0

        for i in range(len(s)):
            if s[i] == '[':
                opening += 1
            else:
                closing += 1
                if opening < closing:
                    swaps += 1
                    opening += 1
                    closing -= 1
        return swaps