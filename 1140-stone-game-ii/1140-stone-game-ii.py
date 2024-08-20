class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sufsum = [0] * n
        sufsum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            sufsum[i] = sufsum[i + 1] + piles[i]
        
        memo = {}
        def dp(i, m):
            if i >= n: # no more tiles
                return 0
            if i + 2 * m >= n: # all remaining tiles are claimable
                return sufsum[i]
            if (i, m) in memo:
                return memo[(i, m)]
            max_claim = 0
            for x in range(1, 2 * m + 1):
                if i + x >= n:
                    break
                max_claim = max(max_claim, sufsum[i] - dp(i + x, max(m, x)))
            memo[(i, m)] = max_claim
            return max_claim

        answer = dp(0, 1)
        return answer