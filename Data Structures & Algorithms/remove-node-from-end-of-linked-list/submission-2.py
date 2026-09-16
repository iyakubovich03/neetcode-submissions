# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        forward=dummy
        anotherDummy=forward
        for _ in range(n):
            dummy=dummy.next
        while dummy and dummy.next:
            dummy=dummy.next
            forward=forward.next
        forward.next=forward.next.next 
        return anotherDummy.next
        