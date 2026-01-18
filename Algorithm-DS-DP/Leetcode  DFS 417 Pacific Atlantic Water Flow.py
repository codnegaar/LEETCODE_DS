'''
Leetcode  DFS 417 Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and the Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix height where heights[r][c] represent the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rainwater can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates results where result[i] = [ri, ci] denotes that rainwater can flow from cell (ri, ci) to both the Pacific and Atlantic oceans. 

Example 1:
        Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
        [0,4]: [0,4] -> Pacific Ocean 
               [0,4] -> Atlantic Ocean
        [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
               [1,3] -> [1,4] -> Atlantic Ocean
        [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
               [1,4] -> Atlantic Ocean
        [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
               [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
        [3,0]: [3,0] -> Pacific Ocean 
               [3,0] -> [4,0] -> Atlantic Ocean
        [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
               [3,1] -> [4,1] -> Atlantic Ocean
        [4,0]: [4,0] -> Pacific Ocean 
               [4,0] -> Atlantic Ocean
        Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
        
Example 2:
        Input: heights = [[1]]
        Output: [[0,0]]
        Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:
        m == heights.length
        n == heights[r].length
        1 <= m, n <= 200
        0 <= heights[r][c] <= 105

'''

class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    m = len(heights)
    n = len(heights[0])
    dirs = [0, 1, 0, -1, 0]
    qP = collections.deque()
    qA = collections.deque()
    seenP = [[False] * n for _ in range(m)]
    seenA = [[False] * n for _ in range(m)]

    for i in range(m):
      qP.append((i, 0))
      qA.append((i, n - 1))
      seenP[i][0] = True
      seenA[i][n - 1] = True

    for j in range(n):
      qP.append((0, j))
      qA.append((m - 1, j))
      seenP[0][j] = True
      seenA[m - 1][j] = True

    def bfs(q: deque, seen: List[List[bool]]):
      while q:
        i, j = q.popleft()
        h = heights[i][j]
        for k in range(4):
          x = i + dirs[k]
          y = j + dirs[k + 1]
          if x < 0 or x == m or y < 0 or y == n:
            continue
          if seen[x][y] or heights[x][y] < h:
            continue
          q.append((x, y))
          seen[x][y] = True

    bfs(qP, seenP)
    bfs(qA, seenA)

    return [[i, j] for i in range(m) for j in range(n) if seenP[i][j] and seenA[i][j]]



