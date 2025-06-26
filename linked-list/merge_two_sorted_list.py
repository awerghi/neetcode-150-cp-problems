from typing import Optional


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    # 1-> 2 -> 4
    # 1 -> 3 -> 5
    # res = 1 -> 1 -> 2 -> 3 -> 4 -> 5

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)
        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2


        return head

    def print_linked_list(self,head):
        current = head
        while current.next is not None :
            print(current.val)
            current = current.next
        print(current.val)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3


node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(5)
node4.next = node5
node5.next = node6


list1 = node1
list2 = node4

s = Solution()
head = s.mergeTwoLists(list1,list2)
s.print_linked_list(head)