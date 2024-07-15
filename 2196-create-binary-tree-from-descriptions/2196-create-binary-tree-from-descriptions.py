# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for desc in descriptions:
            p, c, is_left = desc
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            if is_left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            children.add(c)
        
        for k, v in nodes.items():
            if k not in children:
                return v
