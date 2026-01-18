'''

Leetcode Graph 417 Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
        Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
        [0,4]: [0,4] -> Pacific Ocean 
               [0,4] -> Atlantic Ocean
        [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
               [1,3] -> [1,4] -> Atlantic Ocean
        [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
               [1,4] -> Atlantic Ocean
        [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
               [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
        [3,0]: [3,0] -> Pacific Ocean 
               [3,0] -> [4,0] -> Atlantic Ocean
        [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
               [3,1] -> [4,1] -> Atlantic Ocean
        [4,0]: [4,0] -> Pacific Ocean 
               [4,0] -> Atlantic Ocean
        Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
        Input: heights = [[1]]
        Output: [[0,0]]
        Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
         
Constraints:
        m == heights.length
        n == heights[r].length
        1 <= m, n <= 200
        0 <= heights[r][c] <= 105
'''
from typing import List, Deque
import collections

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Find all coordinates in a matrix where water can flow to both the Pacific and Atlantic oceans.

        Args:
            heights (List[List[int]]): 2D list representing heights of each cell in a matrix.

        Returns:
            List[List[int]]: List of coordinates where water can flow to both oceans.
        """
        
        m, n = len(heights), len(heights[0])  # Matrix dimensions
        directions = [0, 1, 0, -1, 0]  # Used to move in 4 directions
        pacific_queue, atlantic_queue = collections.deque(), collections.deque()
        
        # Create visited matrices for cells reachable by each ocean
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        
        # Initialize borders for each ocean
        for i in range(m):
            pacific_queue.append((i, 0))  # Left border (Pacific)
            atlantic_queue.append((i, n - 1))  # Right border (Atlantic)
            pacific_reachable[i][0] = True
            atlantic_reachable[i][n - 1] = True

        for j in range(n):
            pacific_queue.append((0, j))  # Top border (Pacific)
            atlantic_queue.append((m - 1, j))  # Bottom border (Atlantic)
            pacific_reachable[0][j] = True
            atlantic_reachable[m - 1][j] = True

        def bfs(queue: Deque, reachable: List[List[bool]]):
            """Perform BFS to mark cells reachable by the current ocean."""
            while queue:
                i, j = queue.popleft()
                current_height = heights[i][j]
                
                # Explore all 4 directions
                for k in range(4):
                    x, y = i + directions[k], j + directions[k + 1]
                    
                    # Skip if out of bounds or already visited or height decreases
                    if x < 0 or x >= m or y < 0 or y >= n or reachable[x][y] or heights[x][y] < current_height:
                        continue
                    
                    # Mark as reachable and add to queue
                    reachable[x][y] = True
                    queue.append((x, y))

        # Perform BFS for each ocean
        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)

        # Collect cells reachable by both oceans
        return [[i, j] for i in range(m) for j in range(n) if pacific_reachable[i][j] and atlantic_reachable[i][j]]
