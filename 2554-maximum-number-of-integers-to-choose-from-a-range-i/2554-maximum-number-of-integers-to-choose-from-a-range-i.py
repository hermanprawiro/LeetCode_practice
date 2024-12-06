class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banset = set([num for num in banned if num <= n])
        answer = 0
        total = 0
        for i in range(1, n + 1):
            if i not in banset and total + i <= maxSum:
                total += i
                answer += 1
        return answer
