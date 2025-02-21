# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.count = defaultdict(int)
        root.val = 0
        self._recover(root)

    def find(self, target: int) -> bool:
        return target in self.count

    def _recover(self, root: Optional[TreeNode]):
        self.count[root.val] += 1
        if root.left:
            root.left.val = root.val * 2 + 1
            self._recover(root.left)
        
        if root.right:
            root.right.val = root.val * 2 + 2
            self._recover(root.right)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)