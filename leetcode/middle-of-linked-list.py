# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # repr
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
    
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(node: Optional[ListNode]) -> int:
            if node is None:
                return []
            return traverse(node.next) + [node]
        l = traverse(head)
        return l[len(l)//2 if len(l) % 2 == 0 else math.ceil(len(l)/2)]

# test m,ethod middleNode of SOlution class
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print(sol.middleNode(head))