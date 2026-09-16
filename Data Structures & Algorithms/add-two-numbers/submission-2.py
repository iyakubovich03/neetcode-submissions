# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1,pointer2=l1,l2
        carry=0
        dummy=ListNode()
        returnValue=dummy

        while pointer1 or pointer2:
            val1=pointer1.val if pointer1 else 0
            val2=pointer2.val if pointer2 else 0

            currentSum=val1+val2+carry
            nodeValue=(currentSum%10)
            carry=currentSum//10

            dummy.next=ListNode(nodeValue)
            dummy=dummy.next
            
            if pointer1:
                pointer1=pointer1.next
            if pointer2:
                pointer2=pointer2.next
        if carry:
            dummy.next=ListNode(carry)
        return returnValue.next