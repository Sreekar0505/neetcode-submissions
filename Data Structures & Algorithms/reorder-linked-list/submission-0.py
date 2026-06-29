# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.left = head

        def reorder(right):
            if not right:
                return False
            
            flag = reorder(right.next)

            if flag:
                return flag

            if self.left is None or self.left == right or self.left.next == right:
                right.next = None 
                return True

            temp = self.left.next
            self.left.next = right
            right.next = temp

            self.left = temp
            return False
        
        reorder(head)
 

