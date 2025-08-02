from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.gen_parentheses = []
        stack = []
        def backtrack(direct_parentheses,indirect_parentheses):
            if direct_parentheses == n and indirect_parentheses == n :
                self.gen_parentheses.append(''.join(stack))

            if direct_parentheses < n :
                stack.append('(')
                backtrack(direct_parentheses+1,indirect_parentheses)
                stack.pop()

            if indirect_parentheses < direct_parentheses :
                stack.append(')')
                backtrack(direct_parentheses,indirect_parentheses+1)
                stack.pop()
        backtrack(0,0)
        return self.gen_parentheses

s = Solution()
print(s.generateParenthesis(3)) # output : ['((()))', '(()())', '(())()', '()(())', '()()()']


