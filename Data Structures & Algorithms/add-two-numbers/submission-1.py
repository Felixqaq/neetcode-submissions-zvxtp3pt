# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addBit = 0
        l1head = l1
        pre = None
        while l1 and l2:
            l1.val += l2.val + addBit
            addBit = 0
            if l1.val >= 10:
                addBit = 1
                l1.val -= 10
            pre = l1
            l1 = l1.next
            l2 = l2.next

        if l2: 
            pre.next = l2
            l1 = l2
        while l1:
            l1.val += addBit
            addBit = 0
            if l1.val >= 10:
                addBit = 1
                l1.val -= 10
            pre = l1
            l1 = l1.next
        if addBit:
            pre.next = ListNode(1)
        return l1head