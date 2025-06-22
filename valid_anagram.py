# PROBLEM STATEMENT : https://neetcode.io/problems/is-anagram?list=neetcode150
# Author aw.ahmed.werghi@gmail.com



# solution 1
# sort both strings and compare
# Time complexity = O(n log(n))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = Solution()
print(s.isAnagram("jar","jam")) # False
print(s.isAnagram("racecar","racecar")) # True

# solution 2:
# make two tables of 26, number of alphabetic carachters,
# compare them after filling them
# Time complexity = O(n)

class OptimalSolution:

    def fill_table_with_string (self, s : str):
        alpha_s = [0 for i in range(26)]
        for i in range(len(s)):
            alpha_s[ord(s[i])-ord('a')] += 1

        return alpha_s

    def isAnagram(self, s: str, t: str) -> bool:
        alpha_s = self.fill_table_with_string(s)
        alpha_t = self.fill_table_with_string(t)

        for i in range(26):
            if alpha_t[i] == alpha_s[i]:
                continue
            else:
                return False

        return True



s = OptimalSolution()
print(s.isAnagram("jar","jam")) # False
print(s.isAnagram("racecar","racecar")) # True

