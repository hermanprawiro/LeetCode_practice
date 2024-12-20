# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        level = 0
        queue = [root]
        while queue:
            cur_queue = []
            for _ in range(len(queue)):
                cur_node = queue.pop(0)
                cur_queue.append(cur_node)
                # add child for next batch processing
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            if level % 2 == 1: # when odd level, we swap their value
                left, right = 0, len(cur_queue) - 1
                while left < right:
                    cur_queue[left].val, cur_queue[right].val = cur_queue[right].val, cur_queue[left].val
                    left += 1
                    right -= 1
            level += 1
        return root