# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        if count == 1:
            return None

        cur = head
        pre = None
        if count-n == 0:
            return head.next
        for i in range(count-n):
            print(cur.val)
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return head