# Problem statement : https://neetcode.io/problems/valid-sudoku?list=neetcode150
# Author aw.ahmed.werghi@gmail.com


# Valid sudo problem

from typing import List

class Solution:
    def isDistinct(self,nums):
        return len(nums) == len(set(nums))

    def isValidRecord (self, record : List[str]) -> bool:
        nums = [num for num in record if num != '.']
        return self.isDistinct(nums)
        for elt in record:
            if elt == "." or 1 <= int(elt) <= 9:
                continue
            else:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ensure that each row does not contain duplicates and contains digits from 1 to 9 (bool ok1)
        # ensure that each column does not contain duplicates and contains digits from 1 to 9 (bool ok2)
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates (bool ok3)

        # first verification, each row contains distinct digits between 1 and 9
        for i in range(len(board)):
            if self.isValidRecord(board[i]):
                continue
            else:
                return False

        # second verification, each column contains distinct digits between 1 and 9
        for i in range(len(board)):
            column = [board[k][i] for k in range(9)]
            print(column)
            if self.isValidRecord(column):
                continue
            else:
                return False

        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates (bool ok3)
        for i in range(0,9,3):
            for j in range(0,9,3):
                column = []
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        column.append(board[k][l])
                if self.isValidRecord(column):
                    continue
                else:
                    return False
        return True

s = Solution()
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
# -> False


print(s.isValidSudoku(board))

board1 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

# -> True


print(s.isValidSudoku(board1))


board2 = [[".",".","4",".",".",".","6","3","."],
          [".",".",".",".",".",".",".",".","."],
          ["5",".",".",".",".",".",".","9","."],
          [".",".",".","5","6",".",".",".","."],
          ["4",".","3",".",".",".",".",".","1"],
          [".",".",".","7",".",".",".",".","."],
          [".",".",".","5",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."]]

print(s.isValidSudoku(board2))