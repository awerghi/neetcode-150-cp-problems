# PROBLEM STATEMENT : https://neetcode.io/problems/reverse-string?list=neetcode250
# Author aw.aw.ahmed.werghi@gmail.com

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1

        while start < end :
            aux = s[start]
            s[start] = s[end]
            s[end] = aux
            start += 1
            end -= 1

s = Solution()
slist = ["n","e","e","t"]
s.reverseString(slist)
print(slist) # -> output : ['t', 'e', 'e', 'n']

slist2 = ["r","a","c","e","c","a","r"]
s.reverseString(slist2)
print(slist2) # -> output : ['r', 'a', 'c', 'e', 'c', 'a', 'r']