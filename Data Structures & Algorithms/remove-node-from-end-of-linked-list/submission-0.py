# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy.next
        l = 0
        while (curr):
            l+=1
            curr = curr.next
        ind = l-n
        curr = dummy
        while (ind > 0):
            curr = curr.next
            ind-=1
        curr.next = curr.next.next
        return dummy.next
