# Author aw.ahmed.werghi@gmail.com
# problem statement : https://neetcode.io/problems/search-for-word?list=neetcode150

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        self.ok = False

        def backtrack(i, j, k, path):

            if k == len(word):
                self.ok = True
                return

            if i < 0 or i >= n or j < 0 or j >= m:
                return

            if (i, j) in path:
                return

            if word[k] != board[i][j]:
                return

            path.add((i, j))

            backtrack(i, j + 1, k + 1, path)
            backtrack(i, j - 1, k + 1, path)
            backtrack(i + 1, j, k + 1, path)
            backtrack(i - 1, j, k + 1, path)

            path.remove((i, j))

        for i in range(n):
            for j in range(m):
                backtrack(i, j, 0, set())
                if self.ok:
                    return True

        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))