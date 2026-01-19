'''
130 Surrounded Regions 
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
        Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        Explanation: Notice that an 'O' should not be flipped if:
        - It is on the border, or
        - It is adjacent to an 'O' that should not be flipped.
        The bottom 'O' is on the border, so it is not flipped.
        The other three 'O' form a surrounded region, so they are flipped.

Example 2:
        Input: board = [["X"]]
        Output: [["X"]]
 

Constraints:
        m == board.length
        n == board[i].length
        1 <= m, n <= 200
        board[i][j] is 'X' or 'O'.
'''
class Solution:
  def solve(self, board: List[List[str]]) -> None:
      #Do not return anything, modify board in-place instead.
    if not board:
      return

    m = len(board)
    n = len(board[0])
    dirs = [0, 1, 0, -1, 0]
    q = collections.deque()

    for i in range(m):
      for j in range(n):
        if i * j == 0 or i == m - 1 or j == n - 1:
          if board[i][j] == 'O':
            q.append((i, j))
            board[i][j] = '*'

    # Mark grids that stretch from four sides with '*'
    while q:
      i, j = q.popleft()
      for k in range(4):
        x = i + dirs[k]
        y = j + dirs[k + 1]
        if x < 0 or x == m or y < 0 or y == n:
          continue
        if board[x][y] != 'O':
          continue
        q.append((x, y))
        board[x][y] = '*'

    for row in board:
      for i, c in enumerate(row):
        row[i] = 'O' if c == '*' else 'X'



# Second solution
class Solution:
    """
    Solve Surrounded Regions Problem

    Modifies the board in-place:
    - Captures all regions surrounded by 'X' (i.e., flips 'O' -> 'X').
    - Ensures 'O' on the borders or connected to borders remain unchanged.

    Time Complexity: O(n), where n = ROWS * COLS
    Space Complexity: O(1) (in-place DFS traversal)
    
    Parameters:
    - board: List[List[str]] - A 2D grid containing 'O' and 'X'.
    
    Example:
    Input:
    board = [
      ["X", "X", "X", "X"],
      ["X", "O", "O", "X"],
      ["X", "X", "O", "X"],
      ["X", "O", "X", "X"]
    ]
    
    Output:
    board = [
      ["X", "X", "X", "X"],
      ["X", "X", "X", "X"],
      ["X", "X", "X", "X"],
      ["X", "O", "X", "X"]
    ]
    """

    def solve(self, board: list[list[str]]) -> None:
        """
        Main method to solve the surrounded regions problem.

        Args:
        - board: A 2D list representing the grid.

        Returns:
        None. Modifies the board in place.
        """
        ROWS, COLS = len(board), len(board[0])  # Get grid dimensions
        
        # Helper function to perform DFS for border-connected 'O's
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return  # Exit condition: Out of bounds or not 'O'
            board[r][c] = "T"  # Temporarily mark as 'T'
            dfs(r + 1, c)  # Explore down
            dfs(r - 1, c)  # Explore up
            dfs(r, c + 1)  # Explore right
            dfs(r, c - 1)  # Explore left

        # Step 1: Capture border-connected 'O' regions
        for r in range(ROWS):
            for c in [0, COLS - 1]:  # Only first and last columns
                if board[r][c] == "O":
                    dfs(r, c)  # Start DFS for boundary 'O'
        
        for r in [0, ROWS - 1]:  # Only first and last rows
            for c in range(COLS):
                if board[r][c] == "O":
                    dfs(r, c)  # Start DFS for boundary 'O'
        
        # Step 2: Convert surrounded 'O's to 'X' and restore border-connected 'T' to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  # Surrounded 'O' -> 'X'
                elif board[r][c] == "T":
                    board[r][c] = "O"  # Restore 'T' -> 'O'

# Unit Test
if __name__ == "__main__":
    # Test Case Example
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    expected_output = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    sol = Solution()
    sol.solve(board)
    
    print("Modified Board:")
    for row in board:
        print(row)
    assert board == expected_output, "Test Failed!"
    print("Test Passed!")

"""
References:
- Python List: https://docs.python.org/3/tutorial/datastructures.html
- DFS Algorithm: https://docs.python.org/3/library/collections.html
"""
 

