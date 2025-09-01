# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/palindrome-partitioning?list=neetcode150

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_str_list = {'9': ['w', 'x', 'y', 'z'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                           '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v']}

        if len(digits) == 0: return []
        dp_digits = []
        dp_digits.append(digits_str_list[digits[0]])
        for i in range(1, len(digits)):
            digits_aux = []
            for option in digits_str_list[digits[i]]:
                for last_option in dp_digits[i - 1]:
                    digits_aux.append((last_option + option))
            dp_digits.append(digits_aux)

        return dp_digits[-1]
