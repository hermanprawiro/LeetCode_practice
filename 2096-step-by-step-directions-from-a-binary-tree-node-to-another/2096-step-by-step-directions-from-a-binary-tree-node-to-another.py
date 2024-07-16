# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        paths_start = []
        paths_dest = []

        self.dfs(root, startValue, paths_start)
        self.dfs(root, destValue, paths_dest)

        while len(paths_start) and len(paths_dest) and paths_start[-1] == paths_dest[-1]:
            paths_start.pop()
            paths_dest.pop()

        return "".join("U" * len(paths_start)) + "".join(paths_dest[::-1])
            

    def dfs(self, root: TreeNode, val: int, paths: str) -> bool:
        if root.val == val:
            return True
        if root.left and self.dfs(root.left, val, paths):
            paths += "L"
        elif root.right and self.dfs(root.right, val, paths):
            paths += "R"
        return len(paths)
        
        