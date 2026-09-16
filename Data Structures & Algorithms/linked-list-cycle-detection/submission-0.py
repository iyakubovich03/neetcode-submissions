# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x=0
        while x<1000:
            if head:
                head=head.next
            else:
                return False
            x+=1
        return True