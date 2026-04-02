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
        nodeLoc = {}
        newHead = Node(0)
        cur = head
        ncur = newHead

        while cur:
            ncur.next = Node(cur.val)
            
            ncur = ncur.next
            nodeLoc[cur] = ncur
            cur = cur.next
            
        newHead = newHead.next
        ncur = newHead
        cur = head
        while cur:
            if cur.random:
                ncur.random = nodeLoc[cur.random]
            else:
                ncur.random = None
            cur = cur.next
            ncur = ncur.next

        return newHead

