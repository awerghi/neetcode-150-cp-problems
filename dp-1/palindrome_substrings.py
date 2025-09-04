class Solution:
    def palindome(self, str):
        aux = list(str).copy()
        aux.reverse()
        return list(str) == aux

    def countSubstrings(self, s: str) -> int:
        dp_palindrome = [[s[0]]]
        for i in range(1, len(s)):
            aux = [s[i]]
            for p in range(len(dp_palindrome[i - 1])):
                aux.append(dp_palindrome[i - 1][p] + s[i])
            dp_palindrome.append(aux)

        dp_palindrome_collection = []
        for elt in dp_palindrome:
            dp_palindrome_collection += elt

        palindrome_count = 0
        for elt in dp_palindrome_collection:
            if self.palindome(elt):
                palindrome_count += 1
        return palindrome_count
