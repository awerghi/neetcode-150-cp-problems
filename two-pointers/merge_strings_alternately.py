# PROBLEM STATEMENT : https://neetcode.io/problems/merge-strings-alternately?list=neetcode250
# Author aw.ahmed.werghi@gmail.com


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str_word = ""
        n1 = len(word1)
        n2 = len(word2)
        for i in range(min(n1, n2)):
            merged_str_word += word1[i] + word2[i]

        if n1 > n2:
            merged_str_word += word1[n2:]
        elif n1 < n2:
            merged_str_word += word2[n1:]

        return merged_str_word
