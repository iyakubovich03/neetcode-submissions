# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum=ListNode(0,head)
        counter1=head
        counter2= dum
        for i in range(n):
            counter1=counter1.next
        while counter1:
            counter2=counter2.next
            counter1=counter1.next
        counter2.next=counter2.next.next
        return dum.next

        
        