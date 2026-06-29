# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reorder(left,right):
            if not right:
                return [left,False]

            left,flag = reorder(left,right.next)

            if flag:
                return [left,flag]

            if not left or left == right or left.next == right:
                right.next = None
                return [left,True]
            
            temp = left.next
            left.next = right
            right.next = temp

            return [temp,False]

        reorder(head,head)

            
            