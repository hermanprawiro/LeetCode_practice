class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Arr is a permutation of int in range [0, n-1],
        so when sorted, the arr[i] should be == i.
        When we find arr[i] > i, then arr[:i] should be in the same chunk as arr[i].
        When arr is already sorted, arr[i] == i, so each num can form individual chunk.
        """
        answer = 0
        cur_max = 0
        for i, num in enumerate(arr):
            cur_max = max(cur_max, num)
            if cur_max == i:
                answer += 1
        return answer

