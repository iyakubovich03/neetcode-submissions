# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
    #uses two pointer fast pointer
        curr=head
        fast=head
        while fast!=None:
            if fast.next == None:
                return False
            curr=curr.next
            fast=fast.next.next
            if (curr == fast):
                return True
        return False
