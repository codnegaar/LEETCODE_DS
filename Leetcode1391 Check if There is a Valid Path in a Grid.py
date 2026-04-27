'''
Leetcode1391 Check if There is a Valid Path in a Grid
 
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:
        1 which means a street connecting the left cell and the right cell.
        2 which means a street connecting the upper cell and the lower cell.
        3 which means a street connecting the left cell and the lower cell.
        4 which means a street connecting the right cell and the lower cell.
        5 which means a street connecting the left cell and the upper cell.
        6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) 
and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.
Return true if there is a valid path in the grid or false otherwise. 

Example 1:
        Input: grid = [[2,4,3],[6,5,2]]
        Output: true
        Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

Example 2:
        Input: grid = [[1,2,1],[1,2,1]]
        Output: false
        Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)

Example 3:
        Input: grid = [[1,1,2]]
        Output: false
        Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
 

Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        1 <= grid[i][j] <= 6
'''
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
        dirs = [up, down, left, right]
        mapping ={
            1 : {right : right, left : left},
            2 : {up : up, down : down},
            3 : {right : down, up : left},
            4 : {up : right, left : down},
            5 : {right : up, down : left},
            6 : {down : right, left : up}
        }
    
        def helper(i, j, move, visited = True):
            if (
                i < 0 or 
                j < 0 or 
                i >= len(grid) or 
                j >= len(grid[0]) or
                (not (move in mapping[grid[i][j]])) or
                (visited and i == 0 and j == 0)
            ):
                return False
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return True
            
            next_move = mapping[grid[i][j]][move]
            di, dj = next_move
            return helper(i + di, j + dj, next_move)
        
        for direction in dirs:
            if helper(0, 0, direction, visited = False):
                return True
        
        return False




