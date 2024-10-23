# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1 pass bfs
        # init prev sum as the root val
        # for each node, update its val as (prev_sum - its_val)
        # prev_sum will be the sum of the level, its_val will be sibling sum
        # for each level, accumulate the sum of the level below as cur_sum
        # update the children value to its sibling sum
        # update prev_sum = cur_sum
        if not root:
            return root
        nodes = deque()
        nodes.append(root)
        prev_sum = root.val
        while nodes:
            n_nodes = len(nodes)
            cur_sum = 0
            for _ in range(n_nodes):
                node = nodes.popleft()
                node.val = prev_sum - node.val
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val

                if node.left:
                    cur_sum += node.left.val
                    node.left.val = sibling_sum
                    nodes.append(node.left)
                if node.right:
                    cur_sum += node.right.val
                    node.right.val = sibling_sum
                    nodes.append(node.right)
            prev_sum = cur_sum
        return root