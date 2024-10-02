class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hash_map = {}
        rank = 1
        for num in sorted(arr):
            if num not in hash_map:
                hash_map[num] = rank
                rank += 1
        result = []
        for num in arr:
            result.append(hash_map[num])
        return result
        