class Solution:
    def palindome(self, str):
        aux = list(str).copy()
        aux.reverse()
        return list(str) == aux

    def longestPalindrome(self, s: str) -> str:
        dp_palindrome = [[s[0]]]
        for i in range(1, len(s)):
            aux = [s[i]]
            for p in range(len(dp_palindrome[i - 1])):
                if i == 2: print(dp_palindrome[i - 1][p])
                aux.append(dp_palindrome[i - 1][p] + s[i])
            dp_palindrome.append(aux)

        dp_palindrome_collection = []
        for elt in dp_palindrome:
            dp_palindrome_collection += elt

        longest_palindrome_len = 0
        longest_palindrome_str = ""
        for elt in dp_palindrome_collection:
            if self.palindome(elt) and len(elt) > longest_palindrome_len:
                longest_palindrome_str = elt
                longest_palindrome_len = len(elt)
        return longest_palindrome_str
