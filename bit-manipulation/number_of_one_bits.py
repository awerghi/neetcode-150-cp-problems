# Author aw.aw.ahmed.werghi@gmail.com
# PROBLEM STATEMENT : https://neetcode.io/problems/number-of-one-bits?list=neetcode150


class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([elt for elt in str(bin(n)) if elt == '1'])
