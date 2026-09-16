# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        li=ListNode(0,head)
        po=li
        while True:
            yol=self.kthn(po,k)
            if not yol:
                break
            gNext=yol.next
            curr,prev=po.next,yol.next
            while curr!=gNext:  #y does this not work with j using yol.next
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            
            temp=po.next
            po.next=yol
            po=temp
        return li.next
            
    def kthn(self,tit,k):
        while tit and k>0:
            tit=tit.next
            k-=1
        return tit

        