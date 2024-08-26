"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result

        self._helper(root, result)
        return result

    def _helper(self, node: 'Node', result: List[int]) -> None:
        if not node:
            return
        
        for child in node.children:
            self._helper(child, result)
        result.append(node.val)
        