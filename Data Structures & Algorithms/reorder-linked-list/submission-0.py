# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #this will iterate all the way until the slow pointer is on the last part of first list

        
        secP=slow.next
        prev=slow.next=None
        while(secP):
            temp=secP.next
            secP.next=prev
            prev=secP
            secP=temp
        # this iteration flipped the link list 

        first,end=head,prev
        while(end):
            temp1,temp2=first.next,end.next
            first.next=end
            end.next=temp1
            first,end=temp1,temp2
        # this iterates over the two pointer at the top and at the end it gives the head next value of linked list until the second reversed list runs out to null 


            
        