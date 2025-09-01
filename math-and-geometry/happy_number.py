# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/non-cyclical-number?list=neetcode150

class Solution:
    def sum_digits(self, number: int) -> int:
        return sum([pow(int(elt), 2) for elt in list(str(number))])

    def isHappy(self, n: int) -> bool:
        sum_digits = self.sum_digits(n)
        list_sum_digits = [sum_digits]
        while sum_digits != 1:
            sum_digits = self.sum_digits(sum_digits)
            if sum_digits in list_sum_digits:
                return False
            list_sum_digits.append(sum_digits)

        return True
