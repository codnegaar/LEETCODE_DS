'''
Leetcode 1878 Get Biggest Three Rhombus Sums in a Grid
 
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​.
The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell.
Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:
        Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.
        Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them. 

Example 1:
        Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
        Output: [228,216,211]
        Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
        - Blue: 20 + 3 + 200 + 5 = 228
        - Red: 200 + 2 + 10 + 4 = 216
        - Green: 5 + 200 + 4 + 2 = 211

Example 2:
        Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [20,9,8]
        Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
                      - Blue: 4 + 2 + 6 + 8 = 20
                      - Red: 9 (area 0 rhombus in the bottom right corner)
                      - Green: 8 (area 0 rhombus in the bottom middle)

Example 3:
        Input: grid = [[7,7,7]]Output: [7]
        Explanation: All three possible rhombus sums are the same, so return [7].
         
Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 50
        1 <= grid[i][j] <= 105
'''


import heapq
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        left_prefix = [[0]*m for _ in range(n)]
        for j in range(m):
            left_prefix[0][j] = grid[0][j]
        for i in range(1, n):
            for j in range(m):
                if j + 1 < m:
                    left_prefix[i][j] = grid[i][j] + left_prefix[i-1][j+1]
                else:
                    left_prefix[i][j] = grid[i][j]

        right_prefix = [[0]*m for _ in range(n)]
        for j in range(m):
            right_prefix[0][j] = grid[0][j]
        for i in range(1, n):
            for j in range(m):
                if j - 1 >= 0:
                    right_prefix[i][j] = grid[i][j] + right_prefix[i-1][j-1]
                else:
                    right_prefix[i][j] = grid[i][j]
        heap = []
        for i in range(n):
            for j in range(m):
                offset = 0
                while j - offset>= 0 and j + offset < m and i + 2*(offset) < n:
                    if offset == 0:
                        temp = grid[i][j]
                    else:
                        temp = left_prefix[i+offset][j-offset] - left_prefix[i][j] + grid[i][j] + right_prefix[i+offset][j+offset] - right_prefix[i][j] + right_prefix[i+2*offset][j]-right_prefix[i+offset][j-offset] + left_prefix[i+2*offset][j] - left_prefix[i+offset][j+offset] - grid[i+2*offset][j]
                    if temp not in heap:
                        heapq.heappush(heap, temp)
                        if len(heap) > 3:
                            heapq.heappop(heap)
                    offset+=1
        heap.sort(key = lambda x: -x)
        return heap

                    
