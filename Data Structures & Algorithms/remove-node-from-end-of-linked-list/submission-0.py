# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        li=ListNode(0,head)
        po=li
        y=head
        while (n>0):
            y=y.next
            n=n-1
        while y:
            y=y.next
            po=po.next
        po.next=po.next.next
        return li.next





        

        