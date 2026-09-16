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
        middlePointer=self.reverseNodes(middlePointer)
        print(f"this is the middle pointer {middlePointer.val}")
        dummy=head

        while middlePointer:
            print(f"current start {dummy.val}")
            temp=dummy.next
            temp2=middlePointer.next
            dummy.next=middlePointer
            if not middlePointer.next:
                return
            middlePointer.next=temp
            dummy=middlePointer.next
            middlePointer=temp2
            
        
        
        
    def reverseNodes(self,node):
        prev=None
        current=node
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev