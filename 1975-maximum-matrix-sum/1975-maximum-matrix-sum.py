class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # count all the num in matrix and keep track of
        # abs sum, num of negatives, abs min number
        # if #negatives is even, the answer is the abs sum
        # it #negatives is odd, we want the abs min number as negative
        # so answer is abs_sum - (2 * abs_min_number)
        # because abs_sum already contains abs_min_number once
        n_negatives = 0
        abs_sum = 0
        abs_min_num = float('inf')
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                n_negatives += 1 if num < 0 else 0
                abs_sum += abs(num)
                abs_min_num = min(abs_min_num, abs(num))
        if n_negatives % 2: # odd
            return abs_sum - 2 * abs_min_num
        else: # even
            return abs_sum