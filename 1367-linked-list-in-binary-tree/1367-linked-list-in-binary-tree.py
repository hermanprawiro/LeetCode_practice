# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return (
            self.dfs(head, root) or
            self.isSubPath(head, root.left) or
            self.isSubPath(head, root.right)
        )
        
    def dfs(self, list_node: Optional[ListNode], tree_node: Optional[TreeNode]) -> bool:
        if not list_node: # end of linked-list means we found a match
            return True
        if not tree_node: # end of tree means we haven't found match
            return False
        if list_node.val != tree_node.val:
            return False
        return self.dfs(list_node.next, tree_node.left) or self.dfs(list_node.next, tree_node.right)
        