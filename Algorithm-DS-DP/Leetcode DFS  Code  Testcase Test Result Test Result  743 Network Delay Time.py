'''

Leetcode DFS  Code  Testcase Test Result Test Result  743 Network Delay Time.py


You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1. 

Example 1:
        Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2

Example 2:
        Input: times = [[1,2,1]], n = 2, k = 1
        Output: 1

Example 3:
        Input: times = [[1,2,1]], n = 2, k = 2
        Output: -1 

Constraints:
        1 <= k <= n <= 100
        1 <= times.length <= 6000
        times[i].length == 3
        1 <= ui, vi <= n
        ui != vi
        0 <= wi <= 100
        All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

'''

class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    graph = [[] for _ in range(n)]

    for u, v, w in times:
      graph[u - 1].append((v - 1, w))

    return self._dijkstra(graph, k - 1)

  def _dijkstra(self, graph: List[List[Tuple[int, int]]], src: int) -> int:
    dist = [math.inf] * len(graph)

    dist[src] = 0
    minHeap = [(dist[src], src)]  # (d, u)

    while minHeap:
      d, u = heapq.heappop(minHeap)
      for v, w in graph[u]:
        if d + w < dist[v]:
          dist[v] = d + w
          heapq.heappush(minHeap, (dist[v], v))

    maxDist = max(dist)
    return maxDist if maxDist != math.inf else -1
