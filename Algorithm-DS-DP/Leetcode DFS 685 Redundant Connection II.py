'''

Leetcode DFS 685 Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, 
plus every node has exactly one parent, except for the root node which has no parents.
The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi,
where ui is a parent of child vi. Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers,
return the answer that occurs last in the given 2D-array.

Example 1:
        Input: edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]

Example 2:
        Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
        Output: [4,1]
 
Constraints:
        n == edges.length
        3 <= n <= 1000
        edges[i].length == 2
        1 <= ui, vi <= n
        ui != vi

'''

class UnionFind:
  def __init__(self, n: int):
    self.id = list(range(n))
    self.rank = [0] * n

  def unionByRank(self, u: int, v: int) -> bool:
    i = self._find(u)
    j = self._find(v)
    if i == j:
      return False
    if self.rank[i] < self.rank[j]:
      self.id[i] = j
    elif self.rank[i] > self.rank[j]:
      self.id[j] = i
    else:
      self.id[i] = j
      self.rank[j] += 1
    return True

  def _find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self._find(self.id[u])
    return self.id[u]


class Solution:
  def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
    ids = [0] * (len(edges) + 1)
    nodeWithTwoParents = 0

    for _, v in edges:
      ids[v] += 1
      if ids[v] == 2:
        nodeWithTwoParents = v

    def findRedundantDirectedConnection(skippedEdgeIndex: int) -> List[int]:
      uf = UnionFind(len(edges) + 1)

      for i, edge in enumerate(edges):
        if i == skippedEdgeIndex:
          continue
        if not uf.unionByRank(edge[0], edge[1]):
          return edge

      return []

    # If there is no edge with two ids
    # We don't have to skip any edge
    if nodeWithTwoParents == 0:
      return findRedundantDirectedConnection(-1)

    for i in reversed(range(len(edges))):
      _, v = edges[i]
      if v == nodeWithTwoParents:
        # Try to delete edges[i]
        if not findRedundantDirectedConnection(i):
          return edges[i]
