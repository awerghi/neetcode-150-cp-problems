# Author aw.aw.ahmed.werghi@gmail.com
# PROBLEM STATEMENT : https://neetcode.io/problems/find-duplicate-integer?list=neetcode150

from typing import List, Counter


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        occ = Counter(nums)
        for k,v in occ.items():
            if v > 1:
                return k
        return -1


s = Solution()
print(s.findDuplicate([1,2,3,4,4])) # output : answer : 4