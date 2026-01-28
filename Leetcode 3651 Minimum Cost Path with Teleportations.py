'''
Leetcode 3651 Minimum Cost Path with Teleportations

You are given a m x n 2D integer array grid and an integer k. You start at the top-left cell (0, 0) and your goal is to reach the bottom‐right cell (m - 1, n - 1).
There are two types of moves available:
Normal move: You can move right or down from your current cell (i, j), i.e. you can move to (i, j + 1) (right) or (i + 1, j) (down). The cost is the value of the destination cell.
Teleportation: You can teleport from any cell (i, j), to any cell (x, y) such that grid[x][y] <= grid[i][j]; the cost of this move is 0. You may teleport at most k times.
Return the minimum total cost to reach cell (m - 1, n - 1) from (0, 0).

Example 1:
        Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2
        Output: 7        
        Explanation:        
                Initially we are at (0, 0) and cost is 0.        
                Current Position	Move	New Position	Total Cost
                (0, 0)	Move Down	(1, 0)	0 + 2 = 2
                (1, 0)	Move Right	(1, 1)	2 + 5 = 7
                (1, 1)	Teleport to (2, 2)	(2, 2)	7 + 0 = 7
                The minimum cost to reach bottom-right cell is 7.

Example 2:
        Input: grid = [[1,2],[2,3],[3,4]], k = 1
        Output: 9
        Explanation:
                Initially we are at (0, 0) and cost is 0.
                Current Position	Move	New Position	Total Cost
                (0, 0)	Move Down	(1, 0)	0 + 2 = 2
                (1, 0)	Move Right	(1, 1)	2 + 3 = 5
                (1, 1)	Move Down	(2, 1)	5 + 4 = 9
                The minimum cost to reach bottom-right cell is 9.

Constraints:
        2 <= m, n <= 80
        m == grid.length
        n == grid[i].length
        0 <= grid[i][j] <= 104
        0 <= k <= 10
'''


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # dp[i][j][n_teleport]: list[list[int]] =>
        # minimum cost to get to (i, j) by using at most n_teleport teleportations
        # Size of dp => m*n*k
        # Initialization:
        # dp[i][j][0] = min(
        #     dp[i-1][j][0],  # move down
        #     dp[i][j-1][0]   # move right
        # ) + grid[i][j]
        
        # Transitions:
        # dp[i][j][n_teleport] = min(
        #     dp[i-1][j][n_teleport] + grid[i][j],  # move down
        #     dp[i][j-1][n_teleport] + grid[i][j],  # move right 
        #     min(
        #         dp[ip][jp][n_teleport-1]
        #     ) for all ip, jp s.t. grid[ip][jp] >= grid[i][j]
        # )
        # To compute:
        #     min(
        #         dp[ip][jp][n_teleport-1]
        #     ) for all ip, jp s.t. grid[ip][jp] >= grid[i][j]
        # We have to be clever otherwise TLE
        
        # We will use min_cost_from_cells_of_value_v: list[int] of size max(grid) + 1
        # min_cost_from_cells_of_value_v[v] = minimum cost from all the dp[i][j][n_teleport - 1] s.t. grid[i][j] = v
        # This can be computed in O(max(grid) + m*n)
        
        # We will use min_cost_from_cells_above_value_v: list[int] of size max(grid) + 1
        # min_cost_from_cells_above_value_v[v] = minimum cost from all the dp[i][j][n_teleport - 1] s.t. grid[i][j] >= v
        # This can be computed in O(max(grid))
        # min_cost_from_cells_above_value_v[v] = min(
        #     min_cost_from_cells_above_value_v[v+1],
        #     min_cost_from_cells_of_value_v[v]
        # )

        dp: list[list[list[int]]] = [
            [
                [
                    10**18 for _ in range(k+1)
                ] for _ in range(len(grid[0]))
            ] for _ in range(len(grid))
        ]
        
        dp[0][0][0] = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i != 0 or j != 0:
                    dp[i][j][0] = min(
                        dp[i-1][j][0] if i != 0 else 10**18,  # move down
                        dp[i][j-1][0] if j != 0 else 10**18   # move right
                    ) + grid[i][j]
        
        max_grid: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_grid = max(max_grid, grid[i][j])
        
        for n_teleport in range(1, k+1):
            min_cost_from_cells_of_value_v: list[int] = [10**18 for _ in range(max_grid + 1)]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    min_cost_from_cells_of_value_v[grid[i][j]] = min(
                        min_cost_from_cells_of_value_v[grid[i][j]],
                        dp[i][j][n_teleport-1]
                    )
            min_cost_from_cells_above_value_v: list[int] = [10**18 for _ in range(max_grid + 1)]
            min_cost_from_cells_above_value_v[max_grid] = min_cost_from_cells_of_value_v[max_grid]
            for v in range(max_grid-1, -1, -1):
                min_cost_from_cells_above_value_v[v] = min(
                    min_cost_from_cells_above_value_v[v+1],
                    min_cost_from_cells_of_value_v[v]
                )
            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    dp[i][j][n_teleport] = min(
                        (dp[i-1][j][n_teleport] + grid[i][j]) if i != 0 else 10**18,  # move down
                        (dp[i][j-1][n_teleport] + grid[i][j]) if j != 0 else 10**18,  # move right
                        min_cost_from_cells_above_value_v[grid[i][j]]
                    )
        
        return dp[-1][-1][k]
        
