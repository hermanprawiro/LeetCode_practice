class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 0
        direction = 1
        for _ in range(time):
            if i == 0:
                direction = 1
            if i == (n - 1):
                direction = -1
            i += direction
        return i + 1