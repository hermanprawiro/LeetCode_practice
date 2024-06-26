# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self._arr = []
        self.traverse(root)
        return self.arrayToBST(0, len(self._arr) - 1)

    def traverse(self, root: TreeNode) -> None:
        if not root:
            return

        self.traverse(root.left)
        self._arr.append(root.val)
        self.traverse(root.right)
    
    def arrayToBST(self, start: int, end: int) -> TreeNode:
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(self._arr[mid])
        root.left = self.arrayToBST(start, mid - 1)
        root.right = self.arrayToBST(mid + 1, end)
        return root
        