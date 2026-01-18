'''
Leetcode Graph 787 Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array of flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, and return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:          
          Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
          Output: 700
          Explanation:
          The graph is shown above.
          The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
          Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
        Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
        Output: 200
        Explanation:
        The graph is shown above.
        The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:        
        Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
        Output: 500
        Explanation:
        The graph is shown above.
        The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:
        1 <= n <= 100
        0 <= flights.length <= (n * (n - 1) / 2)
        flights[i].length == 3
        0 <= fromi, toi < n
        fromi != toi
        1 <= pricei <= 104
        There will not be any multiple flights between two cities.
        0 <= src, dst, k < n
        src != dst

'''

class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = [[] for _ in range(n)]

    for u, v, w in flights:
      graph[u].append((v, w))

    return self._dijkstra(graph, src, dst, k)

  def _dijkstra(self, graph: List[List[Tuple[int, int]]], src: int, dst: int, k: int) -> int:
    dist = [[math.inf for _ in range(k + 2)] for _ in range(len(graph))]

    dist[src][k + 1] = 0
    minHeap = [(dist[src][k + 1], src, k + 1)]  # (d, u, stops)

    while minHeap:
      d, u, stops = heapq.heappop(minHeap)
      if u == dst:
        return d
      if stops == 0:
        continue
      for v, w in graph[u]:
        if d + w < dist[v][stops - 1]:
          dist[v][stops - 1] = d + w
          heapq.heappush(minHeap, (dist[v][stops - 1], v, stops - 1))

    return -1

