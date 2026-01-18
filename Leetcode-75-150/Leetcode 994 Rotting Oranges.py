'''
Leetcode 994 Rotting Oranges 

You are given an m x n grid where each cell can have one of three values:
        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.
        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
        Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4
        
Example 2:
        Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
        Input: grid = [[0,2]]
        Output: 0
        Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 10
        grid[i][j] is 0, 1, or 2.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


# second 
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Computes the minimum time required for all fresh oranges to rot.

        Parameters:
        grid (List[List[int]]): A 2D list representing the grid where:
            - 0 represents an empty cell
            - 1 represents a fresh orange
            - 2 represents a rotten orange

        Returns:
        int: The minimum number of minutes required for all oranges to rot,
             or -1 if it is impossible.
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize the queue with all rotten oranges and count fresh ones
        for r, c in ((r, c) for r in range(rows) for c in range(cols)):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

        # If no fresh oranges, return 0 immediately
        if fresh_count == 0:
            return 0

        # Possible 4-directional moves
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        # BFS to spread the rot
        while queue and fresh_count:
            for _ in range(len(queue)):  # Process all rotting oranges at the current level
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check if the new cell is within bounds and has a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark it as rotten
                        queue.append((nr, nc))
                        fresh_count -= 1  # Decrease fresh orange count
            
            minutes += 1  # Increase the time after processing one level

        return minutes if fresh_count == 0 else -1


# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cases(self):
        self.assertEqual(self.solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)
        self.assertEqual(self.solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)
        self.assertEqual(self.solution.orangesRotting([[0,2]]), 0)
        self.assertEqual(self.solution.orangesRotting([[0]]), 0)
        self.assertEqual(self.solution.orangesRotting([[1]]), -1)
        self.assertEqual(self.solution.orangesRotting([[2,2,2],[2,1,2],[2,2,2]]), 1)

if __name__ == "__main__":
    unittest.main()

