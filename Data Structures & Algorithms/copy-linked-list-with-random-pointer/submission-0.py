"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        l=head
        old= {None : None}
        while l:
            copy=Node(l.val)
            old[l]=copy
            l=l.next #this is used to iterate over the linked list n put it in a dictionary
        l=head
        while(l): #this is hten used to iterate for hte linked list and make a copy from the dicitionary
            copy=old[l]
            copy.next=old[l.next]
            copy.random=old[l.random]
            l=l.next
        return old[head] #returns the first node of the head


        