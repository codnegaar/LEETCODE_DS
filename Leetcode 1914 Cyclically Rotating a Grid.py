'''
Leetcode 1914 Cyclically Rotating a Grid
 
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.
The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:
A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent 
element in the counter-clockwise direction. An example rotation is shown below:

Return the matrix after applying k cyclic rotations to it. 

Example 1:
        Input: grid = [[40,10],[30,20]], k = 1
        Output: [[10,20],[40,30]]
        Explanation: The figures above represent the grid at every state.

Example 2:
        Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
        Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
        Explanation: The figures above represent the grid at every state.
 
Constraints:
        m == grid.length
        n == grid[i].length
        2 <= m, n <= 50
        Both m and n are even integers.
        1 <= grid[i][j] <= 5000
        1 <= k <= 109

'''

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for l in range(layers):
            vals = []
            top, left = l, l
            bottom, right = m - l - 1, n - l - 1

            # top row
            for j in range(left, right):
                vals.append(grid[top][j])
            # right col
            for i in range(top, bottom):
                vals.append(grid[i][right])
            # bottom row
            for j in range(right, left, -1):
                vals.append(grid[bottom][j])
            # left col
            for i in range(bottom, top, -1):
                vals.append(grid[i][left])

            length = len(vals)
            shift = k % length
            vals = vals[shift:] + vals[:shift]

            idx = 0
            # put back
            for j in range(left, right):
                grid[top][j] = vals[idx]; idx += 1
            for i in range(top, bottom):
                grid[i][right] = vals[idx]; idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = vals[idx]; idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = vals[idx]; idx += 1

        return grid
