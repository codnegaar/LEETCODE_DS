'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
        Input: points = [[1,1],[2,2],[3,3]]
        Output: 3
        
Example 2:
        Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        Output: 4
        
 Constraints:
        1 <= points.length <= 300
        points[i].length == 2
        -104 <= xi, yi <= 104

'''

class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    ans = 0

    def gcd(a: int, b: int) -> int:
      return a if b == 0 else gcd(b, a % b)

    def getSlope(p: List[int], q: List[int]) -> Tuple[int, int]:
      dx = p[0] - q[0]
      dy = p[1] - q[1]
      if dx == 0:
        return (0, p[0])
      if dy == 0:
        return (p[1], 0)
      d = gcd(dx, dy)
      return (dx // d, dy // d)

    for i, p in enumerate(points):
      slopeCount = collections.defaultdict(int)
      samePoints = 1
      maxPoints = 0
      for j in range(i + 1, len(points)):
        q = points[j]
        if p == q:
          samePoints += 1
        else:
          slope = getSlope(p, q)
          slopeCount[slope] += 1
          maxPoints = max(maxPoints, slopeCount[slope])
      ans = max(ans, samePoints + maxPoints)

    return and


# Second solution
from typing import List
from collections import defaultdict
from math import inf
import unittest

class Solution:
    """
    A class to solve the problem of finding the maximum number of points that lie on the same straight line.
    """
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Finds the maximum number of points that lie on the same straight line.

        Parameters:
        points (List[List[int]]): A list of points represented as [x, y] coordinates.

        Returns:
        int: The maximum number of points that lie on a single straight line.
        """
        if len(points) <= 2:
            # If there are 2 or fewer points, they always lie on the same line.
            return len(points)

        def find_slope(p1: List[int], p2: List[int]) -> float:
            """
            Helper function to calculate the slope between two points.

            Parameters:
            p1, p2 (List[int]): Two points represented as [x, y].

            Returns:
            float: The slope of the line passing through p1 and p2. If the line is vertical, return infinity.
            """
            x1, y1 = p1
            x2, y2 = p2
            if x1 == x2:  # Vertical line
                return inf
            return (y1 - y2) / (x1 - x2)

        max_points = 1  # Initialize the result variable.

        for i, p1 in enumerate(points):
            slopes = defaultdict(int)  # Dictionary to store slopes and their frequency.
            for p2 in points[i + 1:]:
                slope = find_slope(p1, p2)  # Calculate the slope between points p1 and p2.
                slopes[slope] += 1  # Count the points with the same slope.
                max_points = max(max_points, slopes[slope])  # Update the maximum points on the same line.

        return max_points + 1  # Add 1 to include the starting point itself.

# Example usage:
if __name__ == "__main__":
    points = [[1, 1], [2, 2], [3, 3], [4, 4]]
    solution = Solution()
    print("Maximum points on a line:", solution.maxPoints(points))  # Output: 4


# Unit tests
class TestSolution(unittest.TestCase):
    def test_maxPoints(self):
        sol = Solution()
        self.assertEqual(sol.maxPoints([[1, 1], [2, 2], [3, 3]]), 3)
        self.assertEqual(sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4)
        self.assertEqual(sol.maxPoints([[0, 0]]), 1)
        self.assertEqual(sol.maxPoints([[1, 1], [2, 2], [3, 3], [1, 2]]), 3)
        self.assertEqual(sol.maxPoints([[1, 1], [2, 2], [3, 3], [4, 4], [0, 1]]), 4)


# Run the tests
unittest.main(argv=[''], exit=False)

# Changes made:
# - Added a docstring for the `maxPoints` function and `find_slope` helper method.
# - Improved efficiency by avoiding redundant checks and utilizing a `defaultdict`.
# - Added `unittest` test cases to ensure the function works for a variety of scenarios.
# - Improved readability by renaming variables and adding comments to explain each step.
# - Example usage provided for easier understanding of functionality.


