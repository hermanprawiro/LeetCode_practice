# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()

        i1 = l1
        i2 = l2
        j = result

        while i1 is not None or i2 is not None:
            sum_val = j.val
            if i1 is not None:
                sum_val += i1.val
                i1 = i1.next

            if i2 is not None:
                sum_val += i2.val
                i2 = i2.next
            
            remainder = 0
            if sum_val > 9:
                remainder = sum_val // 10
                sum_val = sum_val % 10
            
            j.val = sum_val

            if i1 is not None or i2 is not None or remainder > 0:
                j.next = ListNode(val=remainder)
                j = j.next

        return result



            