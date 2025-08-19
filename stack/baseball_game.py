# PROBLEM STATEMENT : https://neetcode.io/problems/baseball-game?list=neetcode250
# Author aw.aw.ahmed.werghi@gmail.com

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in range(len(operations)):
            if operations[i] == "+":
                scores.append(scores[-1] + scores[-2])
            elif operations[i] == "C":
                scores.pop()
            elif operations[i] == "D":
                scores.append(scores[-1] * 2)
            else:
                scores.append(int(operations[i]))
            print(scores)
        return sum(scores)
