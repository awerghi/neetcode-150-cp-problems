import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for node in lists:
            while node:
                heapq.heappush(pq, node)
                node = node.next
        if not pq: return None

        nodes = []
        while pq:
            current_node = heapq.heappop(pq)
            nodes.append(current_node)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        return nodes[0]