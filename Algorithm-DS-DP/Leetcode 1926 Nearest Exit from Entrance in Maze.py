'''

Leetcode 1926 Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, 
where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find
the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:
        Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
        Output: 1
        Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
        Initially, you are at the entrance cell [1,2].
        - You can reach [1,0] by moving 2 steps left.
        - You can reach [0,2] by moving 1 step up.
        It is impossible to reach [2,3] from the entrance.
        Thus, the nearest exit is [0,2], which is 1 step away.
        
Example 2:
        Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
        Output: 2
        Explanation: There is 1 exit in this maze at [1,2].
        [1,0] does not count as an exit since it is the entrance cell.
        Initially, you are at the entrance cell [1,0].
        - You can reach [1,2] by moving 2 steps right.
        Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
        Input: maze = [[".","+"]], entrance = [0,0]
        Output: -1
        Explanation: There are no exits in this maze.
         
Constraints:
        maze.length == m
        maze[i].length == n
        1 <= m, n <= 100
        maze[i][j] is either '.' or '+'.
        entrance.length == 2
        0 <= entrancerow < m
        0 <= entrancecol < n
        entrance will always be an empty cell.

'''


from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Finds the nearest exit from the maze starting from the given entrance.
        Parameters:
            maze (List[List[str]]): The maze represented as a 2D grid.
            entrance (List[int]): The starting point coordinates [row, col].
        Returns:
            int: The minimum number of steps to reach an exit, or -1 if no exit exists.
        """
        # Get the dimensions of the maze
        m, n = len(maze), len(maze[0])
        # Directions to move in the maze: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initialize BFS queue and seen set with entrance point
        queue = deque([(entrance[0], entrance[1])])
        seen = {(entrance[0], entrance[1])}
        steps = 0

        while queue:
            # Iterate through nodes at current level
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # Explore all four possible directions
                for di, dj in directions:
                    x, y = i + di, j + dj
                    # Skip out-of-bounds or visited cells, or walls ('+')
                    if not (0 <= x < m and 0 <= y < n) or (x, y) in seen or maze[x][y] == '+':
                        continue
                    # If this cell is on the boundary and is not the entrance, it's an exit
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return steps + 1
                    # Mark cell as seen and add it to the queue
                    queue.append((x, y))
                    seen.add((x, y))
            # Increment the number of steps for each level of BFS
            steps += 1

        # Return -1 if no exit is found
        return -1

# Example usage:
# sol = Solution()
# maze = [['+', '+', '.', '+'],
#         ['.', '.', '.', '+'],
#         ['+', '+', '+', '.']]
# entrance = [1, 0]
# print(sol.nearestExit(maze, entrance))  # Output: 2


