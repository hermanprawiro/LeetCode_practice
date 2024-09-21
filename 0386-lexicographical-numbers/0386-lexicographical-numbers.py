class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        cur = 1
        for _ in range(n):
            result.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur >= n or cur % 10 == 9:
                    cur //= 10
                cur += 1
        return result
