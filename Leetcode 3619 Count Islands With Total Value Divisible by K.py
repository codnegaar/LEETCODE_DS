'''

Leetcode 3619 Count Islands With Total Value Divisible by K
 
You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

 

Example 1:


Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:


Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.


'''
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                total, grid[i][j], island = grid[i][j], 0, [(i, j)]  # a new island: take the first cell's value and sink it
                for x, y in island:  # the list grows while we walk it: a BFS queue
                    for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= a < m and 0 <= b < n and grid[a][b]:
                            total += grid[a][b]
                            grid[a][b] = 0  # sink it so it's counted once
                            island.append((a, b))
                ans += total % k == 0
        return ans
