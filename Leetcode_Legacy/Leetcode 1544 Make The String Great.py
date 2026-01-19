'''
1544 Make The String Great

Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
        0 <= i <= s.length - 2
        s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
        To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.        
        Return the string after making it good. The answer is guaranteed to be unique under the given constraints.        
        Notice that an empty string is also good.

Example 1:
        Input: s = "leEeetcode"
        Output: "leetcode"
        Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
        Input: s = "abBAcC"
        Output: ""
        Explanation: We have many possible scenarios, and all lead to the same answer. For example:
        "abBAcC" --> "aAcC" --> "cC" --> ""
        "abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
        Input: s = "s"
        Output: "s"
 
Constraints:
        1 <= s.length <= 100
        s contains only lower and upper case English letters.

'''
class Solution:
    def makeGood(self, s: str) -> str:
        sb = list(s)
        flag = 0
        while flag == 0 and len(sb) > 0:
            flag = 1
            i = 0
            while i < len(sb) - 1:
                if self.isGreat(sb, i):
                    del sb[i:i+2]
                    flag = 0
                i += 1
        return ''.join(sb)

    def isGreat(self, sb, i):
        return ord(sb[i]) == ord(sb[i + 1]) + 32 or ord(sb[i]) == ord(sb[i + 1]) - 32


# second solution
import heapq
from collections import defaultdict
from typing import List

class Solution(object):
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Build the adjacency list for the graph
        adj = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        # Max-heap to prioritize paths with higher probabilities
        maxHeap = [(-1.0, start_node)]
        # Track the maximum probability to reach each node
        maxProb = [0.0] * n
        maxProb[start_node] = 1.0

        while maxHeap:
            # Get the current node with the highest probability
            current_prob, node = heapq.heappop(maxHeap)
            current_prob = -current_prob

            # Return the probability if the end node is reached
            if node == end_node:
                return current_prob

            # Explore neighbors
            for neighbor, edge_prob in adj[node]:
                new_prob = current_prob * edge_prob
                if new_prob > maxProb[neighbor]:
                    maxProb[neighbor] = new_prob
                    heapq.heappush(maxHeap, (-new_prob, neighbor))

        # Return 0.0 if the end node is unreachable
        return 0.0

