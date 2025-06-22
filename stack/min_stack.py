# PROBLEM STATEMENT : https://neetcode.io/problems/minimum-stack?list=neetcode150
# Author aw.ahmed.werghi@gmail.com


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()


    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        mini = float('inf')
        aux_stack = self.stack.copy()
        while aux_stack:
            current = aux_stack.pop()
            if current < mini :
                mini = current
        return mini

my_stack = MinStack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(0)
my_stack.getMin()
my_stack.pop()
my_stack.top()
my_stack.getMin()