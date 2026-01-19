'''
Leetcode 1579 Remove Max Number of Edges to Keep Graph Fully Traversable
  
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:
          Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
          Output: 2
          Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

Example 2:
          Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
          Output: 0
          Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

Example 3:
          Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
          Output: -1
          Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

Constraints:
        1 <= n <= 105
        1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
        edges[i].length == 3
        1 <= typei <= 3
        1 <= ui < vi <= n
        All tuples (typei, ui, vi) are distinct.

'''

class UnionFind:
    """A minimalist standalone union-find implementation."""
    def __init__(self, n):
        self.count = n               # number of disjoint sets 
        self.parent = list(range(n)) # parent of given nodes
        self.rank = [1]*n            # rank (aka size) of sub-tree 
        
    def find(self, p):
        """Find with path compression."""
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p]) # path compression 
        return self.parent[p]
    
    def union(self, p, q):
        """Union with ranking."""
        rootP, rootQ = self.find(p), self.find(q)
        if rootP == rootQ: 
            return False
        self.count -= 1 # one more connection => one less disjoint set
        if self.rank[rootP] > self.rank[rootQ]: 
            rootP, rootQ = rootQ, rootP # ensure rootP is smaller
        self.parent[rootP] = rootQ
        if self.rank[rootP] == self.rank[rootQ]:
            self.rank[rootQ] += 1 # increment rank if both ranks are equal
        return True
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa = UnionFind(n) # for Alice
        ufb = UnionFind(n) # for Bob
        
        removable_edges = 0
        # Process type 3 edges first
        for t, u, v in sorted(edges, reverse=True):
            u, v = u - 1, v - 1
            if t == 3:
                if not (ufa.union(u, v) and ufb.union(u, v)):
                    removable_edges += 1
        
        # Process type 1 and 2 edges
        for t, u, v in edges:
            u, v = u - 1, v - 1
            if t == 1:
                if not ufa.union(u, v):
                    removable_edges += 1
            elif t == 2:
                if not ufb.union(u, v):
                    removable_edges += 1
        
        # Check if both Alice's and Bob's graphs are fully connected
        if ufa.count == 1 and ufb.count == 1:
            return removable_edges
        else:
            return -1

# Example usage:
# solution = Solution()
# n = 4
# edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# print(solution.maxNumEdgesToRemove(n, edges)) # Expected output: 2
