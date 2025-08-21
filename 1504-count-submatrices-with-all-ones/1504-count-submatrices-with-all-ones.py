class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n_col = len(mat[0])

        heights = [0] * n_col
        answer = 0
        for row in mat:
            for i, val in enumerate(row):
                heights[i] = 0 if val == 0 else heights[i] + 1
            stack = [(-1, 0, 1)]
            for i, val in enumerate(heights):
                while stack[-1][2] >= val:
                    stack.pop()
                j, prev, _ = stack[-1]
                cur = prev + (i - j) * val
                stack.append((i, cur, val))
                answer += cur
        
        return answer