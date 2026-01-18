'''
Leetcode_36_Array_Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

'''


from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key=(r/3, c/3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r//3, c//3]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])


# Second Solution
from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a given 9x9 Sudoku board is valid.

        Parameters:
        board (List[List[str]]): A 9x9 list representing a Sudoku board.

        Returns:
        bool: True if the Sudoku board is valid, False otherwise.
        """
        # Sets to track seen numbers in rows, columns, and 3x3 squares
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # Key is (r//3, c//3)

        # Iterate through each cell in the board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # Skip empty cells
                    continue

                # Check if the current value already exists in the corresponding row, column, or square
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                # Add the current value to the respective row, column, and square sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
