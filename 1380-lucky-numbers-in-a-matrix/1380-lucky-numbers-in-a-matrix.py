class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = []
        maxs = matrix[0]
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                maxs[j] = max(maxs[j], matrix[i][j])
            mins.append(min(matrix[i]))

        return list(set(mins) & set(maxs))
