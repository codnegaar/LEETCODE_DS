'''

Leetcode BFS 407 Trapping Rain Water II

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
        Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
        Output: 4
        Explanation: After the rain, water is trapped between the blocks.
        We have two small ponds 1 and 3 units trapped.
        The total volume of water trapped is 4.

Example 2:
        Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
        Output: 10 

Constraints:
        m == heightMap.length
        n == heightMap[i].length
        1 <= m, n <= 200
        0 <= heightMap[i][j] <= 2 * 104

'''

from heapq import heappop, heappush 

class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        # Get the dimensions of the map
        rows, cols = len(height_map), len(height_map[0])
      
        # Initialize a 2D visited array to keep track of processed cells
        visited = [[False] * cols for _ in range(rows)]
      
        # Priority Queue (min heap) to process the cells by height
        min_heap = []
      
        # Initialize the heap with the boundary cells and mark them as visited
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heappush(min_heap, (height_map[i][j], i, j))
                    visited[i][j] = True
      
        # Total amount of trapped water
        trapped_water = 0
      
        # Directions for neighboring cells
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
      
        # Process the cells until the heap is empty
        while min_heap:
            height, x, y = heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within bounds and not visited
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    # Calculate the possible water level difference
                    trapped_water += max(0, height - height_map[nx][ny])
                  
                    # Mark the neighbor as visited
                    visited[nx][ny] = True
                  
                    # Push the neighbor cell onto the heap with the max height
                    # to keep track of the 'water surface' level
                    heappush(min_heap, (max(height, height_map[nx][ny]), nx, ny))
      
        # Return the total accumulated trapped water
        return trapped_water


# Second Solution
from heapq import heappop, heappush
from typing import List

class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        """
        Calculate the total amount of water trapped in a 2D height map.

        Parameters:
        height_map (List[List[int]]): A 2D list representing the height of the terrain.

        Returns:
        int: The total volume of water trapped.
        """
        # Edge case: if the map is too small to trap water
        if not height_map or len(height_map) < 3 or len(height_map[0]) < 3:
            return 0

        rows, cols = len(height_map), len(height_map[0])
        visited = [[False] * cols for _ in range(rows)]  # Track visited cells
        min_heap = []  # Priority queue to process cells by height

        # Initialize the heap with all boundary cells
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heappush(min_heap, (height_map[i][j], i, j))
                    visited[i][j] = True

        trapped_water = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Neighboring directions

        # Process cells in the min-heap
        while min_heap:
            height, x, y = heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Skip if the neighbor is out of bounds or already visited
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    # Calculate trapped water for the neighbor
                    trapped_water += max(0, height - height_map[nx][ny])
                    visited[nx][ny] = True
                    # Push the neighbor with the updated height to the heap
                    heappush(min_heap, (max(height, height_map[nx][ny]), nx, ny))

        return trapped_water


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    height_map = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    print(f"Trapped water: {solution.trapRainWater(height_map)}")  # Expected output: 4


# Unit Tests
import unittest

class TestTrapRainWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        height_map = [
            [1, 4, 3, 1, 3, 2],
            [3, 2, 1, 3, 2, 4],
            [2, 3, 3, 2, 3, 1]
        ]
        self.assertEqual(self.solution.trapRainWater(height_map), 4)

    def test_case2(self):
        height_map = [
            [5, 5, 5, 5],
            [5, 1, 1, 5],
            [5, 1, 1, 5],
            [5, 5, 5, 5]
        ]
        self.assertEqual(self.solution.trapRainWater(height_map), 16)

    def test_case3(self):
        height_map = [[1]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_case4(self):
        height_map = [
            [1, 1, 1, 1],
            [1, 2, 2, 1],
            [1, 2, 2, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_case5(self):
        height_map = []
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

if __name__ == "__main__":
    # Run the test suite
    unittest.main()


