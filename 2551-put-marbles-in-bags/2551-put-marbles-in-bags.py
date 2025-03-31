class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairs = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pairs.sort()

        # there's also weight[0] and weight[n-1], however because the max and min contains this pair, so it cancels out
        # thus, we only need the difference of the sum of the largest k-1 and the smallest k-1
        return sum(pairs[-k+1:]) - sum(pairs[:k-1])