# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        return self._constructTree(preorder, postorder, 0, n - 1, 0)

    def _constructTree(self, preorder, postorder, pre_start, pre_end, post_start):
        """
        In preorder, the parent will appear before its children.
        In postorder, the parent will appear after its children.
        """
        if pre_start > pre_end: # index out of bound
            return None

        root = TreeNode(preorder[pre_start])
        if pre_start == pre_end: # last node, return itself
            return root

        left_root = preorder[pre_start + 1] # left child

        # find num of nodes in the left subtree (inc left_root) by looking at postorder
        n_left = 1
        while postorder[post_start + n_left - 1] != left_root:
            n_left += 1

        root.left = self._constructTree(preorder, postorder, 
            pre_start + 1, 
            pre_start + n_left, 
            post_start
        )
        root.right = self._constructTree(preorder, postorder, 
            pre_start + n_left + 1,
            pre_end,
            post_start + n_left,
        )
        return root