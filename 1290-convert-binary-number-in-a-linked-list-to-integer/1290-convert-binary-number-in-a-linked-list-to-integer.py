# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        answer = 0
        current = head
        while current:
            # 1. Left shift the current decimal value by 1. This is equivalent to
            #    multiplying by 2, making space for the next bit.
            #    Example: if decimal_value is 5 (binary 101), shifting left gives 10 (binary 1010).
            answer = answer << 1

            # 2. Use a bitwise OR to add the value of the current node (0 or 1).
            #    This effectively sets the last bit to the node's value.
            #    Example: 10 | 1 = 11 (decimal)
            #             10 | 0 = 10 (decimal)
            answer |= current.val
            
            current = current.next
        return answer