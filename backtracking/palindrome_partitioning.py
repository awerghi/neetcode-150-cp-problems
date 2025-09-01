# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/palindrome-partitioning?list=neetcode150

from typing import List

class Solution:
    def palindrome(self, s: str) -> bool:
        aux = list(s)
        slist = list(s)
        slist.reverse()

        return aux == slist

    def palindrome_partition(self, partitions: List[str]) -> bool:
        for partition in partitions:
            if not self.palindrome(partition):
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:

        substrings_partitions = []
        substrings_partitions.append([[s[0]]])

        for i in range(1, len(s)):
            aux_partition = []
            for option in substrings_partitions[i - 1]:
                aux = option.copy()
                aux.append(s[i])
                aux1 = option.copy()
                aux1[-1] = aux1[-1] + s[i]
                aux_partition.append(aux)
                aux_partition.append(aux1)

            substrings_partitions.append(aux_partition)

        palindrome_substrings = []
        for substring in substrings_partitions[-1]:
            if self.palindrome_partition(substring):
                palindrome_substrings.append(substring)

        return palindrome_substrings
