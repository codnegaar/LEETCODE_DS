'''
Leetcode 542 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1. 

Example 1:
        Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
        Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
        Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
        Output: [[0,0,0],[0,1,0],[1,2,1]]
         

Constraints:
        m == mat.length
        n == mat[i].length
        1 <= m, n <= 104
        1 <= m * n <= 104
        mat[i][j] is either 0 or 1.
        There is at least one 0 in mat.

'''
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Updates the matrix such that each cell contains the distance to the nearest 0.

        Parameters:
        mat (List[List[int]]): 2D list of integers where 0 represents an empty cell and 1 represents a cell with 1.

        Returns:
        List[List[int]]: 2D list where each element is the distance to the nearest 0.
        """
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        
        # Initialize the queue with all '0' cells and set '1' cells to -1 as a placeholder
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        # Perform BFS from all '0' cells simultaneously
        while q:
            i, j = q.popleft()
            for di, dj in directions:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and mat[x][y] == -1:
                    mat[x][y] = mat[i][j] + 1
                    q.append((x, y))

        return mat

