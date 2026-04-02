# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lis in lists:
            while lis:
                nodes.append(lis.val)
                lis = lis.next
        
        nodes.sort()

        head = ListNode(0)
        cur = head
        for val in nodes:
            cur.next = ListNode(val)
            cur = cur.next

        return head.next