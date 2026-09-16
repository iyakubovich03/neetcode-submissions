# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy

        heap=[]
        for index,node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(heap,(node.val,index,node)) #nlogn
        
        while heap:#total number
            _,index,node=heapq.heappop(heap) #logn
            current.next=node
            current=current.next
            if node.next:
                heapq.heappush(heap,(node.next.val,index,node.next))
        return dummy.next

        #totalNumber *logn 