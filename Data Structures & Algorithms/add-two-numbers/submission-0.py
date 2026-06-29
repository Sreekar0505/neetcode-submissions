# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ret = ListNode(0)
        curr = ret
        while l1 or l2 or carry:
            temp = carry
            if l1:
                temp+=l1.val
                l1 = l1.next
            if l2:
                temp+=l2.val
                l2 = l2.next
            carry = temp//10
            temp = temp%10
            curr.next = ListNode(temp)
            curr = curr.next
        
        return ret.next
            
