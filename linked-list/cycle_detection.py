# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # The idea is to set the first point to node (next.next)
        # the second pointer moves by one, if there is a cycle, pointer first will be identical to second one at a certain level
        # when this happens, break, else if first or second goes to none, that means no cycle has been detected
        # this pb is a known pb in linked list area as slow, faster pointer
        # maybe there is more optimal solution to this problem

        first = head.next.next if head.next is not None else None
        second = head

        while first != second:
            if first is None or second is None:
                return False
            first = first.next.next if first.next is not None else None
            second = second.next if second.next is not None else None
        return True

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2


s = Solution()
print(s.hasCycle(n1))




                
