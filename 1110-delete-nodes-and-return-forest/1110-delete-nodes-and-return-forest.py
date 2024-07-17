# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        answer = []
        s_del = set(to_delete) # convert to set to optimize lookup

        def dfs(root: Optional[TreeNode], is_delete_parent: bool):
            if not root:
                return None
            
            is_delete_current = root.val in s_del
            root.left = dfs(root.left, is_delete_current)
            root.right = dfs(root.right, is_delete_current)

            # if current node will be disjointed, add to answer
            if is_delete_parent and not is_delete_current:
                answer.append(root)
            if is_delete_current:
                return None
            return root
        
        dfs(root, True)
        return answer
        