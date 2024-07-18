# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.answer = 0
        self.dfs(root, distance)
        return self.answer

    def dfs(self, root: Optional[TreeNode], distance: int) -> List[int]:
        # return a list of all leaves and their distance to the current node
        # only if the distance is smaller than the required
        if not root:
            return []
        if not root.left and not root.right:
            return [1]

        left = self.dfs(root.left, distance)
        right = self.dfs(root.right, distance)

        for l in left:
            for r in right:
                if l + r <= distance:
                    self.answer += 1
        
        return [i + 1 for i in left + right if i + 1 < distance]