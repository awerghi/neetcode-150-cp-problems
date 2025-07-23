# PROBLEM STATEMENT : https://neetcode.io/problems/valid-palindrome-ii?list=neetcode250
# Author aw.ahmed.werghi@gmail.com

class Solution:
    def validPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1
        deletions = 1

        while start < end :
            if s[start] != s[end] and deletions == 0 :
                return False
            elif s[start] != s[end] and deletions == 1 :
                if s[start] == s[end-1] :
                    end -= 1
                elif s[start+1] == s[end]:
                    start += 1
                deletions -= 1
            elif s[start] == s[end]:
                start += 1
                end -= 1
        return True



s = Solution()

print(s.validPalindrome("aca")) # -> output : True
print(s.validPalindrome("abbadc")) # -> output : False
print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdj"
                        "gpfdhooxfuupuculmgmqfvnbgtapekouga")) # -> output : True




