# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head.next
        fast=head.next
        while  fast and fast.next and fast.next.next:
            if fast.next.next==slow.next:
                return True
            fast=fast.next.next
            slow=slow.next
        return False