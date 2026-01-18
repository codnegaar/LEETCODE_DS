'''
1466 Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities 
(this network forms a tree). Last year, The ministry of Transport decided to orient the roads in one direction because they are too narrow.
Roads are represented by connections where connections[i] = [ai, bi] means a road from city ai to city bi.
This year, there will be a significant event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit city 0. Return the minimum number of edges changed.
It's guaranteed that each city can reach city 0 after reordering. 

Example 1:
        Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        Output: 3
        Explanation: Change the direction of the edges in red so that each node can reach node 0 (capital).

Example 2:
        Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
        Output: 2
        Explanation: Change the direction of the edges in red so that each node can reach node 0 (capital).
        
Example 3:
        Input: n = 3, connections = [[1,0],[2,0]]
        Output: 0 
        
Constraints:
        2 <= n <= 5 * 104
        connections.length == n - 1
        connections[i].length == 2
        0 <= ai, bi <= n - 1
        ai != bi
'''

from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for con in connections:
            a,b = con
            adj_list[a].append(b)
            adj_list[b].append(-a)
        visited = [0] * n
        def dfs(start,vis):
            res = 0
            for nxt in adj_list[start]:
                if vis[abs(nxt)] == 1:
                    continue
                if nxt > 0:
                    res+=1
                vis[abs(nxt)] = 1
                res += dfs(abs(nxt),vis)
            return res
        visited[0] = 1
        return dfs(0,visited)
