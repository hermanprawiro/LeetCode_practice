# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max_height_except = [0] * 100001
        self.cur_max = 0

        def left_to_right(node, cur_height):
            if not node:
                return
            max_height_except[node.val] = max(max_height_except[node.val], self.cur_max)
            self.cur_max = max(self.cur_max, cur_height)

            left_to_right(node.left, cur_height + 1)
            left_to_right(node.right, cur_height + 1)
        
        def right_to_left(node, cur_height):
            if not node:
                return
            max_height_except[node.val] = max(max_height_except[node.val], self.cur_max)
            self.cur_max = max(self.cur_max, cur_height)

            right_to_left(node.right, cur_height + 1)
            right_to_left(node.left, cur_height + 1)

        left_to_right(root, 0)
        self.cur_max = 0
        right_to_left(root, 0)

        return [max_height_except[q] for q in queries]

            

