'''
Leetcode (Matrix) 1861 Rotating the Box

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, 
or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.

Example 1:
        Input: box = [["#",".","#"]]
        Output: [["."],
                 ["#"],
                 ["#"]]

Example 2:
        Input: box = [["#",".","*","."],
                      ["#","#","*","."]]
        Output: [["#","."],
                 ["#","#"],
                 ["*","*"],
                 [".","."]]

Example 3:
        Input: box = [["#","#","*",".","*","."],
                      ["#","#","#","*",".","."],
                      ["#","#","#",".","#","."]]
        Output: [[".","#","#"],
                 [".","#","#"],
                 ["#","#","*"],
                 ["#","*","."],
                 ["#",".","*"],
                 ["#",".","."]]
 
Constraints:
          m == box.length
          n == box[i].length
          1 <= m, n <= 500
          box[i][j] is either '#', '*', or '.'.


'''
from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        Rotates a 2D grid representing a box 90 degrees clockwise after letting the stones ('#')
        fall to the bottom (rightmost side in the rotated view).

        Parameters:
        - box (List[List[str]]): A 2D grid where:
            '.' represents an empty cell,
            '#' represents a stone,
            '*' represents an obstacle.

        Returns:
        - List[List[str]]: The rotated grid after processing the stones.
        """
        
        rows, cols = len(box), len(box[0])
        
        # Initialize the rotated box with empty cells (rotated dimensions)
        rotated = [['.'] * rows for _ in range(cols)]
        
        # Process each row to let stones fall and then place in the rotated grid
        for i in range(rows):
            # Pointer for the "bottom" position where the next stone can settle
            bottom = cols - 1
            
            # Iterate through the row in reverse (right to left)
            for j in range(cols - 1, -1, -1):
                if box[i][j] == '#':  # Stone
                    rotated[bottom][rows - 1 - i] = '#'
                    bottom -= 1  # Move the bottom pointer up
                elif box[i][j] == '*':  # Obstacle
                    rotated[j][rows - 1 - i] = '*'
                    bottom = j - 1  # Reset the bottom pointer above the obstacle
        
        return rotated
