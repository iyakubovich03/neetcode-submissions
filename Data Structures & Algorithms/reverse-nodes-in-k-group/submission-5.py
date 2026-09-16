# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kAhead=head #set this pointer 
        current=head
        dummy=ListNode(0,head)
        connector=dummy

        while current:
            kAhead=current
            for _ in range(k-1):
                kAhead=kAhead.next
                if not kAhead:
                    return dummy.next

            stopper=kAhead.next
            begginingNode=self.reverseNodes(current,stopper)
            connector.next=begginingNode
            connector=current
            current=stopper
        return dummy.next
        
    def reverseNodes(self,current,stop): #(pass thorugh each twice)
        #this will reverse a group till it reaches a node
        prev=stop
        while True:
            if current==stop:
                break
            temp=current.next
            current.next=prev
            prev=current
            current=temp

        return prev#this will return the start
    #O(N)


        