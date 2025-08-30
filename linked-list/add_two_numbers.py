# Author aw.aw.ahmed.werghi@gmail.com
# PROBLEM STATEMENT : https://neetcode.io/problems/add-two-numbers?list=neetcode150

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


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2 : return l1

        lres = ListNode((l1.val + l2.val) % 10)
        reste = (l1.val + l2.val) // 10

        l1 = l1.next
        l2 = l2.next
        current = lres
        while l1 or l2:
            if not l1:
                current.next = ListNode((l2.val + reste) % 10)
                reste = (l2.val + reste) // 10
                l2 = l2.next
            elif not l2 :
                current.next = ListNode((l1.val + reste) % 10)
                reste = (l1.val + reste) // 10
                l1 = l1.next
            else :
                current.next = ListNode((l1.val + l2.val + reste) % 10)
                reste = (l1.val + l2.val) // 10
                l1 = l1.next
                l2 = l2.next

            current = current.next
        if reste > 0 : current.next = ListNode(reste)
        return lres



s = Solution()
#----------------------------- TEST CASE 1 -----------------------------
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(8)
n5 = ListNode(8)
n6 = ListNode(5)

n1.next = n2
n2.next = n3

n4.next = n5
n5.next = n6

s.addTwoNumbers(n1,n4) # output : answer : [5,7,9]


#----------------------------- TEST CASE 2 -----------------------------

n9 = ListNode(9)
n10 = ListNode(9)
s.addTwoNumbers(n9,n10) # output : answer : [1,8]

