class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result = [0] * 2
        nums = set()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] in nums:
                    result[0] = grid[i][j]
                nums.add(grid[i][j])
        missing = set([i + 1 for i in range(n**2)]) - nums
        result[1] = list(missing)[0] if len(missing) else 0
        return result