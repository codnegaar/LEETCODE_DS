'''
3394 Check if Grid can be Cut into Sections
 
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:
Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.

Example 1:
        Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
        Output: true
        Explanation: The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:
        Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
        Output: true
        Explanation: We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:
        Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
        Output: false
        Explanation: We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

Constraints:
        3 <= n <= 109
        3 <= rectangles.length <= 105
        0 <= rectangles[i][0] < rectangles[i][2] <= n
        0 <= rectangles[i][1] < rectangles[i][3] <= n
        No two rectangles overlap.

'''
from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
        Determines if there are more than two valid vertical or horizontal cuts
        between given rectangles based on edge overlap.

        Parameters:
        - n (int): Number of rectangles
        - rectangles (List[List[int]]): List of rectangles where each rectangle is
          represented as [x_start, y_start, x_end, y_end]

        Returns:
        - bool: True if more than two valid vertical or horizontal cuts exist, False otherwise
        """
        
        # Helper to count cut opportunities along an axis
        def count_cuts(edges: List[List[int]]) -> int:
            edges.sort()  # Sort edges by coordinate
            count = 0
            active = 0

            for pos, typ in edges:
                active += typ
                if active == 0:
                    count += 1
                    if count > 2:
                        return count
            return count

        # Build edge lists: +1 for start, -1 for end
        vertical_edges = []    # [x, type] pairs
        horizontal_edges = []  # [y, type] pairs

        for x1, y1, x2, y2 in rectangles:
            vertical_edges.append([x1, 1])
            vertical_edges.append([x2, -1])
            horizontal_edges.append([y1, 1])
            horizontal_edges.append([y2, -1])

        # Check if we have more than 2 valid cuts on either axis
        return count_cuts(vertical_edges) > 2 or count_cuts(horizontal_edges) > 2
