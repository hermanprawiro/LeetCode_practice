class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1
        prev = word[0]
        for c in word[1:]:
            if c == prev and count < 9:
                count += 1
            else:
                comp += f"{count}{prev}"
                count = 1
                prev = c
        return comp + f"{count}{prev}" # last prefix