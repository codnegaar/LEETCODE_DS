'''
Leetcode 1219 Path with Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:
        Every time you are located in a cell you will collect all the gold in that cell.
        From your position, you can walk one step to the left, right, up, or down.
        You can't visit the same cell more than once.
        Never visit a cell with 0 gold.
        You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:
        Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
        Output: 24
        Explanation:
        [[0,6,0],
         [5,8,7],
         [0,9,0]]
        Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:
        Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
        Output: 28
        Explanation:
        [[1,0,7],
         [2,0,6],
         [3,4,5],
         [0,3,0],
         [9,0,20]]
        Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.         

Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 15
        0 <= grid[i][j] <= 100
        There are at most 25 cells containing gold.

'''


class Solution:
    # Directions arrays for moving in 4 possible directions (right, left, down, up)
    delta_row = [0, 0, 1, -1]
    delta_col = [1, -1, 0, 0]

    def dfs(self, grid, x, y, n, m):
        # Check for out-of-bound indices and if the cell is 0, return 0
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return 0
        
        current_gold = grid[x][y]
        # Mark this cell as visited by setting it to 0
        grid[x][y] = 0
        max_gold = 0
        
        # Explore all four directions
        for i in range(4):
            next_x = x + self.delta_row[i]
            next_y = y + self.delta_col[i]
            # Recursively collect gold and update the maximum gold found
            max_gold = max(max_gold, current_gold + self.dfs(grid, next_x, next_y, n, m))
        
        # Unmark this cell as visited by restoring its original value
        grid[x][y] = current_gold
        return max_gold

    def getMaximumGold(self, grid):
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        max_gold = 0
        
        # Iterate over each cell in the grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:  # Start DFS only from cells with gold
                    # Update the maximum gold found
                    max_gold = max(max_gold, self.dfs(grid, i, j, n, m))
        
        return max_gold
