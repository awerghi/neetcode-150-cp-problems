class Solution:
    def isPalindrome(self, s: str) -> bool:
        first_s_to_check = ""

        for c in s:
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9') :
                first_s_to_check += c

        s_to_check = first_s_to_check.lower()
        print(s_to_check)
        i = 0
        j = len(s_to_check) - 1
        while i <= j :
            if s_to_check[i] != s_to_check[j] :

                return False
            i += 1
            j -= 1
        return True


s = Solution()
print(s.isPalindrome("0P")) # False
print(s.isPalindrome("Was it a car or a cat I saw?")) # True
print(s.isPalindrome("tab a cat")) # False