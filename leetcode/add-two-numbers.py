# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"{self.val} {f' -> {self.next.__repr__()}' if self.next else ''}"
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l1p = l1
        l2p = l2
        l3p = l3
        carry = 0
        while (l1p or l2p):
            l1pv = l2pv = 0
            if l1p:
                l1pv = l1p.val if l1p else 0
                l1p = l1p.next
            if l2p:
                l2pv = l2p.val if l2p else 0
                l2p = l2p.next
            total = l1pv+l2pv+carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            l3.next = ListNode(total, None)
            l3 = l3.next
            
        if carry:
            l3.next = ListNode(1, None)

        return l3p.next
    
sol = Solution()
print(sol.addTwoNumbers(
    ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
    ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
))
