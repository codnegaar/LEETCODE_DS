'''
Leetcode 200 Number of Islands
 
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume 
all four edges of the grid are all surrounded by water. 

Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1


Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
 
Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

'''

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dirs = [0, 1, 0, -1, 0]

    def bfs(r, c):
      q = collections.deque([(r, c)])
      grid[r][c] = '2'  # Mark '2' as visited
      while q:
        i, j = q.popleft()
        for k in range(4):
          x = i + dirs[k]
          y = j + dirs[k + 1]
          if x < 0 or x == m or y < 0 or y == n:
            continue
          if grid[x][y] != '1':
            continue
          q.append((x, y))
          grid[x][y] = '2'  # Mark '2' as visited

    ans = 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1':
          bfs(i, j)



   # Second solution:

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of distinct islands in a grid using DFS.

        Parameters:
        - grid (List[List[str]]): A 2D grid of strings, where '1' represents land and '0' represents water.

        Returns:
        - int: The number of distinct islands found in the grid.
        """
        if not grid or not grid[0]:
            return 0  # Return 0 if grid is empty or invalid

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r: int, c: int):
            """
            Depth-First Search to explore and mark connected land as visited.

            Parameters:
            - r (int): Current row index.
            - c (int): Current column index.
            """
            # Check for out-of-bounds or if the cell is water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            # Mark the current land cell as visited by setting it to '0'
            grid[r][c] = '0'

            # Visit all 4 connected directions (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If land is found, it's the start of a new island
                if grid[i][j] == '1':
                    island_count += 1  # Increment island counter
                    dfs(i, j)           # Mark the entire island as visited

        return island_count

          ans += 1

    return ans
