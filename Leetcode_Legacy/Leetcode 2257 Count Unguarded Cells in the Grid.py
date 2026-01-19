'''

Leetcode 2257 Count Unguarded Cells in the Grid

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
Return the number of unoccupied cells that are not guarded.

Example 1:
        Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
        Output: 7
        Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
        There are a total of 7 unguarded cells, so we return 7.

Example 2:
        Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
        Output: 4
        Explanation: The unguarded cells are shown in green in the above diagram.
        There are a total of 4 unguarded cells, so we return 4.
         

Constraints:
        1 <= m, n <= 105
        2 <= m * n <= 105
        1 <= guards.length, walls.length <= 5 * 104
        2 <= guards.length + walls.length <= m * n
        guards[i].length == walls[j].length == 2
        0 <= rowi, rowj < m
        0 <= coli, colj < n
        All the positions in guards and walls are unique.

'''

class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        """
        Calculate the number of unguarded cells in a grid given the positions of guards and walls.

        Parameters:
        m (int): Number of rows in the grid.
        n (int): Number of columns in the grid.
        guards (list[list[int]]): List of [row, col] positions for the guards.
        walls (list[list[int]]): List of [row, col] positions for the walls.

        Returns:
        int: The number of unguarded cells in the grid.
        """
        vis = [[0] * n for _ in range(m)]  # Initialize grid with all cells unguarded

        # Mark walls and guards
        for r, c in walls:
            vis[r][c] = 2  # Mark as wall
        for r, c in guards:
            vis[r][c] = 3  # Mark as guard

        # Directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Mark guarded cells
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if vis[nr][nc] in (2, 3):  # Stop at wall or guard
                        break
                    vis[nr][nc] = 1  # Mark as guarded
                    nr += dr
                    nc += dc

        # Count unguarded cells directly in a list comprehension
        return sum(cell == 0 for row in vis for cell in row)


