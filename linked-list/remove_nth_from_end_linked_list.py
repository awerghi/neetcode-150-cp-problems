from typing import Optional

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def show(self,head):
        current = head

        while current is not None:
            print(current.val)
            current = current.next

    def get_linked_list_length(self,head:Optional[ListNode]):
        linked_list_length = 0
        current = head
        while current is not None:
            linked_list_length += 1
            current = current.next
        return linked_list_length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linked_list_length = self.get_linked_list_length(head)
        linked_list_length -= n
        if linked_list_length == 0:
            head = head.next
            return head

        i = 0
        current = head
        previous_target = None
        while i < linked_list_length:
            if i == linked_list_length - 1 : previous_target = current
            current = current.next
            i += 1
        previous_target.next = current.next
        return head


s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(6)

n4 = ListNode(8)
n5 = ListNode(10)
n6 = ListNode(12)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

s.show(n1)
print("--------------------")
s.removeNthFromEnd(n1,2)
s.show(n1)
