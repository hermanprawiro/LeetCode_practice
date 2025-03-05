class Solution:
    def coloredCells(self, n: int) -> int:
        answer = 1
        if n == 1:
            return answer
        for i in range(1, n):
            answer += 4 * i
        return answer