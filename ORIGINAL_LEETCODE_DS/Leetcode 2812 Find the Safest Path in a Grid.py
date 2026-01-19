'''
Leetcode 2812 Find the Safest Path in a Grid
 
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

        A cell containing a thief if grid[r][c] = 1
        An empty cell if grid[r][c] = 0
        You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.        
        The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.        
        Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).        
        An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.        
        The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.
        
Example 1:
        Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
        Output: 0
        Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

Example 2:
        Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
        Output: 2
        Explanation: The path depicted in the picture above has a safeness factor of 2 since:
        - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
        It can be shown that there are no other paths with a higher safeness factor.
        
Example 3:
        Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
        Output: 2
        Explanation: The path depicted in the picture above has a safeness factor of 2 since:
        - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
        - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
        It can be shown that there are no other paths with a higher safeness factor.
         
Constraints:
        1 <= grid.length == n <= 400
        grid[i].length == n
        grid[i][j] is either 0 or 1.
        There is at least one thief in the grid.
'''
from collections import deque
import heapq

class Solution:
    def __init__(self):
        # Direction vectors for 4 possible movements (left, right, up, down)
        self.row_dir = [0, 0, -1, 1]
        self.col_dir = [-1, 1, 0, 0]

    def bfs(self, grid, score, n):
        # Initialize queue for BFS
        queue = deque()

        # Populate initial positions of obstacles or sources with score 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    score[i][j] = 0
                    queue.append((i, j))

        # BFS to calculate minimum distance to nearest obstacle/source
        while queue:
            x, y = queue.popleft()

            for d in range(4):
                new_x = x + self.row_dir[d]
                new_y = y + self.col_dir[d]

                if 0 <= new_x < n and 0 <= new_y < n and score[new_x][new_y] > score[x][y] + 1:
                    score[new_x][new_y] = score[x][y] + 1
                    queue.append((new_x, new_y))

    def maximumSafenessFactor(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:  # Start or end is blocked
            return 0

        # Initialize score matrix with 'infinity'
        score = [[float('inf')] * n for _ in range(n)]
        self.bfs(grid, score, n)

        # Priority queue to process the cell with highest safety factor first
        priority_queue = [(-score[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while priority_queue:
            safe, x, y = heapq.heappop(priority_queue)
            safe = -safe  # Convert back to positive since we use negative for max-heap behavior

            if x == n - 1 and y == n - 1:  # Reached bottom-right corner
                return safe

            visited[x][y] = True

            for d in range(4):
                new_x = x + self.row_dir[d]
                new_y = y + self.col_dir[d]

                if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                    next_safe = min(safe, score[new_x][new_y])
                    heapq.heappush(priority_queue, (-next_safe, new_x, new_y))
                    visited[new_x][new_y] = True  # Mark as visited immediately to prevent reprocessing

        return -1  # No valid path to the target
