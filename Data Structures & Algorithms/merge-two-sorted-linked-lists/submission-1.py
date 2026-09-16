# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        bop=temp = ListNode()
        l=list1
        r=list2
        while l and r:
            if l.val>r.val:
                temp.next=r
                r=r.next
            else:
                temp.next=l
                l=l.next
            temp=temp.next
        temp.next= l or r
     
        return bop.next
            
        