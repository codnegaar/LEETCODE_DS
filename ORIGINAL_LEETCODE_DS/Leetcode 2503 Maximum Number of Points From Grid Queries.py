'''

Leetcode 2503 Maximum Number of Points From Grid Queries

You are given an m x n integer matrix grid and an array queries of size k.
Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:
If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, 
and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
Return the resulting array answer.

Example 1:
        Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
        Output: [5,8,1]
        Explanation: The diagrams above show which cells we visit to get points for each query.

Example 2:   
        Input: grid = [[5,2,1],[1,1,2]], queries = [3]
        Output: [0]
        Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
         

Constraints:        
        m == grid.length
        n == grid[i].length
        2 <= m, n <= 1000
        4 <= m * n <= 105
        k == queries.length
        1 <= k <= 104
        1 <= grid[i][j], queries[i] <= 106

'''

import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        For each threshold in queries, count the number of grid cells reachable 
        from the top-left corner (0,0) such that the value of the cell is less 
        than the threshold. The movement is allowed in four directions (up, down, 
        left, right), and we can only move to unvisited cells.

        Parameters:
        grid (List[List[int]]): 2D grid of integers
        queries (List[int]): List of integer thresholds

        Returns:
        List[int]: Number of reachable points for each query
        """
        M, N = len(grid), len(grid[0])
        
        # Pair each query with its original index to restore order later
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        answer = [0] * len(queries)

        # Min-heap for BFS traversal based on cell value
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * N for _ in range(M)]
        visited[0][0] = True

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        count = 0  # Number of cells with value less than current query

        # Process each query in ascending order
        for threshold, query_index in sorted_queries:
            # Continue expanding from the heap while smallest cell is < threshold
            while heap and heap[0][0] < threshold:
                val, i, j = heapq.heappop(heap)
                count += 1

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # Ensure new coordinates are within bounds and not visited
                    if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj]:
                        visited[ni][nj] = True
                        heapq.heappush(heap, (grid[ni][nj], ni, nj))

            answer[query_index] = count

        return answer


# -------------------------------
# Γ£à Example Usage
# -------------------------------

if __name__ == "__main__":
    grid = [
        [1, 3, 5],
        [2, 8, 4],
        [6, 7, 9]
    ]
    queries = [4, 7, 10]

    sol = Solution()
    result = sol.maxPoints(grid, queries)
    print("Result:", result)  # Example Output: [3, 6, 9]
