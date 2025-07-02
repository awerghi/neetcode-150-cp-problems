from typing import Optional

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def merge_two_lists (self,n1 : Optional[ListNode], n2 : Optional[ListNode]):
        current1 = n1
        current2 = n2

        while True:
            next_node_1 = current1.next if current1.next is not None else None
            next_node_2 = current2.next if current2.next is not None else None

            current1.next = current2
            current2.next = next_node_1
            current1 = next_node_1
            current2 = next_node_2

            if current2 is None and current1 is not None:
                current1.next = None
                break
            elif current2 is None and current1 is None:
                break


    def reorderList(self, head: Optional[ListNode]) -> None:


        # 1 - get the middle of the sequence
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow1 = slow.next

        # reverse the second part of the sequence
        last_node = None
        current = slow1
        head1 = slow
        while True and current:
            next_node = current.next if current.next is not None else None
            current.next = last_node
            last_node = current
            current = next_node
            if current is None:
                head1 = last_node
                break
        slow.next = None

        # merge the two parts
        # 2 -> 4 -> 6 -> 8 -> 10 -> 12
        # part 1 : 2 -> 4 -> 6
        # part 2 (reversed) : 12 -> 10 -> 8
        self.merge_two_lists(head,head1)




    def print_linked_list(self,head : Optional[ListNode]) -> None:
        current = head
        while current.next is not None:
            print(current.val)
            current = current.next
        print(current.val)

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


s.reorderList(n1)
print(s.print_linked_list(n1))



