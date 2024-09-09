# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1] * n for _ in range(m)]
        direction = (0, 1)

        r = 0
        c = 0
        while head is not None:
            mat[r][c] = head.val
            head = head.next
            new_r = r + direction[0]
            new_c = c + direction[1]
            if min(new_r, new_c) < 0 or new_r >= m or new_c >= n or mat[new_r][new_c] != -1:
                direction = (direction[1], -direction[0])
            r += direction[0]
            c += direction[1]
        return mat

