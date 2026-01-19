'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton
devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live
(represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors 
(horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the 
current state, where births and deaths occur simultaneously. Given the current state of 
the m x n grid board, return the next state.

 

Example 1:
        Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        
Example 2:
      Input: board = [[1,1],[1,0]]
      Output: [[1,1],[1,1]]
 

Constraints:
      m == board.length
      n == board[i].length
      1 <= m, n <= 25
      board[i][j] is 0 or 1.
'''
class Solution:
  def gameOfLife(self, board: List[List[int]]) -> None:
    m = len(board)
    n = len(board[0])

    for i in range(m):
      for j in range(n):
        ones = 0
        for x in range(max(0, i - 1), min(m, i + 2)):
          for y in range(max(0, j - 1), min(n, j + 2)):
            ones += board[x][y] & 1
        # Any live cell with 2 or 3 live neighbors
        # lives on to the next generation
        if board[i][j] == 1 and (ones == 3 or ones == 4):
          board[i][j] |= 0b10
        # Any dead cell with exactly 3 live neighbors
        # becomes a live cell, as if by reproduction
        if board[i][j] == 0 and ones == 3:
          board[i][j] |= 0b10

    for i in range(m):
      for j in range(n):
        board[i][j] >>= 1




