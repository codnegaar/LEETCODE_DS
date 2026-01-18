'''
547 Number of Provinces 
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
        Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        Output: 2
        
Example 2:
        Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        Output: 3
 
Constraints:
        1 <= n <= 200
        n == isConnected.length
        n == isConnected[i].length
        isConnected[i][j] is 1 or 0.
        isConnected[i][i] == 1
        isConnected[i][j] == isConnected[j][i]
'''
class UnionFind:
  def __init__(self, n: int):
    self.count = n
    self.id = list(range(n))
    self.rank = [0] * n

  def unionByRank(self, u: int, v: int) -> None:
    i = self._find(u)
    j = self._find(v)
    if i == j:
      return
    if self.rank[i] < self.rank[j]:
      self.id[i] = self.id[j]
    elif self.rank[i] > self.rank[j]:
      self.id[j] = self.id[i]
    else:
      self.id[i] = self.id[j]
      self.rank[j] += 1
    self.count -= 1

  def _find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self._find(self.id[u])
    return self.id[u]


class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    uf = UnionFind(n)

    for i in range(n):
      for j in range(i, n):
        if isConnected[i][j] == 1:
          uf.unionByRank(i, j)

    return uf.count
