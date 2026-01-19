'''
Leetcode 1791 Find Center of Star Graph

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Example 1:
        Input: edges = [[1,2],[2,3],[4,2]]
        Output: 2
        Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
        Input: edges = [[1,2],[5,1],[1,3],[1,4]]
        Output: 1
 
Constraints:
        3 <= n <= 105
        edges.length == n - 1
        edges[i].length == 2
        1 <= ui, vi <= n
        ui != vi
        The given edges represent a valid star graph.

'''

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Finds the center of a star graph.

        Args:
            edges (List[List[int]]): The edges of the star graph.

        Returns:
            int: The center node of the star graph.
        """
        # The center of the star graph will be the common node in the first two edges.
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
