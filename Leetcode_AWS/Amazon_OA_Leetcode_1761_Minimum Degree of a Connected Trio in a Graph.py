'''
Letcode 1761. Minimum Degree of a Connected Trio in a Graph (Shopping Patterns)

You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges,
where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi. A connected trio is a set of 
three nodes where there is an edge between every pair of them. The degree of a connected trio is the number of edges where 
one endpoint is in the trio, and the other is not. Return the minimum degree of a connected trio in the graph, or -1 if the
graph has no connected trios.


Example 1:
          Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
          Output: 3
          Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.

'''


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
            
        dict = {n:len(graph[n]) for n in graph}
        
        result = inf
        for n in graph:
            for m in graph[n]:
                for o in graph[n] & graph[m]:
                    result = min(result, dict[n]+dict[m]+dict[o] - 6)
                    graph[o].discard(n)
                graph[m].discard(n)
        return result if result < inf else -1


'''
# Solution (II)
        graph = defaultdict(set)
        degree = defaultdict(int)
        
        for u, v in edges:
            graph[min(u,v)].add(max(u,v))                     
            graph[u] += 1
            graph[v] += 1
            
        res = sys.maxsize
        
        for n1 in range( 1, n+1):
            for n2 in graph[n1]:
                for n3 in graph[n1]:
                    if n3 in graph [n2]:
                        res = min(res, degree[n1] + degree[n2] + degree[n3] -6 )
                        
        return res if res < sys.maxsize  else  -1
        
        
    '''

