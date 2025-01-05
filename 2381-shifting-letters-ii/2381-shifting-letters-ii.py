class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cumshift = [0] * len(s)
        for shift in shifts:
            start, end, direction = shift
            for i in range(start, end + 1):
                cumshift[i] += 1 if direction == 1 else -1
        answer = list(s)
        for i in range(len(s)):
            if cumshift[i] == 0:
                continue
            answer[i] = self.shiftChar(answer[i], cumshift[i])
        return "".join(answer)
        
    def shiftChar(self, c: str, n: int) -> str:
        idx = ord(c) - ord('a')
        idx = (idx + 26 + n) % 26
        return chr(idx + ord('a'))