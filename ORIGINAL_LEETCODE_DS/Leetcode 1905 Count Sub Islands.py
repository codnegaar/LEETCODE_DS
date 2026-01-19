'''
Leetcode 1905 Count Sub Islands

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land).
An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands. 

Example 1:
        Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
        Output: 3
        Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
        The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Example 2:
        Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
        Output: 2 
        Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
        The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

Constraints:
          m == grid1.length == grid2.length
          n == grid1[i].length == grid2[i].length
          1 <= m, n <= 500
          grid1[i][j] and grid2[i][j] are either 0 or 1.

'''
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        r, c = len(grid1), len(grid1[0])
        N = r * c
        parent = list(range(N + 1))
        size = [1] * (N + 1)
        merged = 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal merged
            rootX, rootY = find(x), find(y)
            if rootX == rootY: 
                return False
            if size[rootX] > size[rootY]:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            else:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
            merged += 1
            return True

        countLand = 0
        for i in range(r):
            for j in range(c):
                if grid2[i][j] == 1:
                    idx = i * c + j
                    countLand += 1

                    if i + 1 < r and grid2[i + 1][j] == 1:
                        union(idx, (i + 1) * c + j)

                    if j + 1 < c and grid2[i][j + 1] == 1:
                        union(idx, i * c + (j + 1))

                    if grid1[i][j] == 0:
                        union(idx, N)  # connect to "water" node

        return countLand - merged
