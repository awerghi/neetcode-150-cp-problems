# PROBLEM STATEMENT : https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150
# Author aw.ahmed.werghi@gmail.com

from typing import Optional


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        last_node = None
        while True and head:
            next_node = current.next
            current.next = last_node
            last_node = current
            current = next_node

            if current is None:
                head = last_node
                break
        return head

