# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kAhead=head #set this pointer 

        for _ in range(k-1): #goes forward to check if we can even reverse
            if not kAhead:
                return head
            kAhead=kAhead.next

        stopper=kAhead.next #node to stop reversing by
        dummy=None

        connector=None
        current=head

        while kAhead:
            begginingNode=self.reverseNodes(current,stopper)

            if connector: 
                connector.next=begginingNode
            if not dummy:
                dummy=begginingNode
            if not stopper:
                return dummy

            current,kAhead=stopper,stopper
            connector=begginingNode

            for _ in range(k-1):
                if not kAhead:
                    return dummy
                
                kAhead=kAhead.next
                connector=connector.next
                if not kAhead:
                    return dummy
            
            stopper=kAhead.next
        
    def reverseNodes(self,current,stop):
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
    


        