'''
Leetcode 85 Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
        Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        Output: 6
        Explanation: The maximal rectangle is shown in the above picture.
        
Example 2:
        Input: matrix = [["0"]]
        Output: 0
        
Example 3:
        Input: matrix = [["1"]]
        Output: 1
 
Constraints:
        rows == matrix.length
        cols == matrix[i].length
        1 <= row, cols <= 200

'''
class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0

    ans = 0
    hist = [0] * len(matrix[0])

    def largestRectangleArea(heights: List[int]) -> int:
      ans = 0
      stack = []

      for i in range(len(heights) + 1):
        while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
          h = heights[stack.pop()]
          w = i - stack[-1] - 1 if stack else i
          ans = max(ans, h * w)
        stack.append(i)

      return ans

    for row in matrix:
      for i, num in enumerate(row):
        hist[i] = 0 if num == '0' else hist[i] + 1
      ans = max(ans, largestRectangleArea(hist))

    return and


#second solution
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_area = 0
        histogram = [0] * len(matrix[0])  # Initialize histogram for the matrix column heights

        def largestRectangleArea(heights: List[int]) -> int:
            """Calculate the largest rectangle area in a histogram"""
            max_area = 0
            stack = []

            for i in range(len(heights) + 1):
                # Add a boundary condition using height 0
                current_height = heights[i] if i < len(heights) else 0
                while stack and heights[stack[-1]] > current_height:
                    h = heights[stack.pop()]
                    # Determine the width using the elements in the stack
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

            return max_area

        # Build histogram from matrix and find the maximum area
        for row in matrix:
            for i, value in enumerate(row):
                # If the cell is '0', reset the height, otherwise increment the height
                histogram[i] = histogram[i] + 1 if value == '1' else 0
            # Update the maximum area found using the current row's histogram
            max_area = max(max_area, largestRectangleArea(histogram))

        return max_area

