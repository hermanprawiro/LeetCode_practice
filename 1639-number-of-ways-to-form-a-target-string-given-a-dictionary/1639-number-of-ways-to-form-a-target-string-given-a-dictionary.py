class Solution:
    def charToIdx(self, char: str) -> int:
        return ord(char) - ord('a')

    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        
        dp = [[-1] * m for _ in range(n)]
        freq = [[0] * 26 for _ in range(n)]
        for i in range(len(words)):
            for j in range(n):
                char_idx = self.charToIdx(words[i][j])
                freq[j][char_idx] += 1
        
        return self.getWords(words, target, 0, 0, dp, freq)

    def getWords(
        self, 
        words: List[str],
        target: str,
        words_idx: int,
        target_idx: int,
        dp: List[List[int]],
        freq: List[List[int]],
    ) -> int:
        n = len(words[0])
        m = len(target)

        if target_idx == m:
            return 1
        if words_idx == n or (n - words_idx < m - target_idx):
            return 0

        if dp[words_idx][target_idx] != -1:
            return dp[words_idx][target_idx]
        
        n_ways = 0
        char_idx = self.charToIdx(target[target_idx])
        # no match (skip current words_idx)
        n_ways += self.getWords(words, target, words_idx + 1, target_idx, dp, freq)
        # match (freq * num of choices)
        n_ways += freq[words_idx][char_idx] * self.getWords(words, target, words_idx + 1, target_idx + 1, dp, freq)
        dp[words_idx][target_idx] = n_ways
        return dp[words_idx][target_idx]