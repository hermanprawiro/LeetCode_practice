class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # sort to handle duplicates easier
        result = []
        self.dfs(candidates, 0, target, result, [])
        return result

    def dfs(self, candidates: List[int], idx: int, target: int, result: List[List[int]], path: List[int]) -> None:
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]: # skip duplicates
                continue
            val = candidates[i]
            path.append(val)
            self.dfs(candidates, i + 1, target - val, result, path)
            path.pop() # backtrack
