# PROBLEM STATEMENT : https://neetcode.io/problems/validate-parentheses?list=neetcode150
# Author aw.aw.ahmed.werghi@gmail.com


class Solution:
    def isValid(self, s: str) -> bool:
        complement = {"{" : "}","[" : "]", "(" : ")"}
        right_direction = ["}","]",")"]
        stack_l = []
        stack_r = []
        for elt in s:
            stack_l.append(elt)

        while stack_l:
            current = stack_l.pop()
            if current in right_direction:
                stack_r.append(current)
            else :
                current_r = stack_r.pop() if stack_r else ""
                if complement.get(current) != current_r:
                    return False
                else:
                    continue
        if len(stack_r) == 0 and len(stack_l) == 0:
            return True
        else:
            return False


s = Solution()
print(s.isValid("]"))