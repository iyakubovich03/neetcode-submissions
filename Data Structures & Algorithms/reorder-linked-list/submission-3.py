# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #reverse the first half of the linkedlist 
        #then iterate forward and grab the next and continue untiil nll
        middlePointer,dummyPointer=head,head
        while dummyPointer and dummyPointer.next:
            dummyPointer=dummyPointer.next.next
            middlePointer=middlePointer.next
        temp=middlePointer.next
        middlePointer.next=None
        middlePointer=temp
        middlePointer=self.reverseNodes(middlePointer)
        
        dummy=head

        while middlePointer:
            temp1=middlePointer.next
            temp2=dummy.next

            dummy.next=middlePointer
            middlePointer.next=temp2

            dummy=temp2
            middlePointer=temp1
            
        
        
        
    def reverseNodes(self,node):
        prev=None
        current=node
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev