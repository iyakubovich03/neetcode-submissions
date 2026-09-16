# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head1,head2=head,head
        while head2 and head2.next:
            head2=head2.next.next
            head1=head1.next
            if head1==head2:
                return True
        return False
        