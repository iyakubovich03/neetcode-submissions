
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
        oldNodeMap={None:None} #old nodes to new nodes

        """
        current=head
        pass2=head

        while current:
            oldNodeMap[current]=Node(current.val)
            current=current.next

        while pass2:
            oldNodeMap[pass2].next=oldNodeMap[pass2.next]
            oldNodeMap[pass2].random=oldNodeMap[pass2.random]
            pass2=pass2.next

        return oldNodeMap[head]
        """
        current=head
        nodeMap={None:None}
        while current:
            value=current.val
            nextNode=current.next
            randomNode=current.random
            if current not in nodeMap:
                nodeMap[current]=Node(current.val)
            if nextNode not in nodeMap:
                nodeMap[nextNode]=Node(nextNode.val)
            if randomNode not in nodeMap:
                nodeMap[randomNode]=Node(randomNode.val)
            nodeMap[current].next=nodeMap[nextNode]
            nodeMap[current].random=nodeMap[randomNode]
            current=current.next
        return nodeMap[head]



        