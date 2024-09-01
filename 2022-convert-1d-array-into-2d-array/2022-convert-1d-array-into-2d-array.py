class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        result = []
        for r in range(m):
            i_start = r * n
            i_end = i_start + n
            result.append(original[i_start:i_end])
        return result
        