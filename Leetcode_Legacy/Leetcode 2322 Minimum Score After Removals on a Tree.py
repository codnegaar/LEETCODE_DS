'''

Leetcode 2322 Minimum Score After Removals on a Tree
 
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of 
length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:
Get the XOR of all the values of the nodes for each of the three components respectively.
The difference between the largest XOR value and the smallest XOR value is the score of the pair.
For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, 
and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
Return the minimum score of any possible pair of edge removals on the given tree.

Example 1:
        Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
        Output: 9
        Explanation: The diagram above shows a way to make a pair of removals.
        - The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
        - The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
        - The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
        The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
        It can be shown that no other pair of removals will obtain a smaller score than 9.

Example 2:
        Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
        Output: 0
        Explanation: The diagram above shows a way to make a pair of removals.
        - The 1st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
        - The 2nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
        - The 3rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
        The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
        We cannot obtain a smaller score than 0.
 
Constraints:
        n == nums.length
        3 <= n <= 1000
        1 <= nums[i] <= 108
        edges.length == n - 1
        edges[i].length == 2
        0 <= ai, bi < n
        ai != bi
        edges represents a valid tree.
'''

from typing import List
import sys


class Solution:
    """
    A class to compute the minimum XOR score after removing two edges from a tree.
    """

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        """
        Computes the minimum difference between the maximum and minimum XOR values
        of three components after removing two edges from a tree.

        Parameters:
            nums (List[int]): The value of each node in the tree.
            edges (List[List[int]]): The edges of the tree as [u, v] pairs.

        Returns:
            int: The minimal score (max XOR - min XOR) after two edge removals.
        """

        n = len(nums)

        # Build adjacency list for the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize XOR values and subtree tracking
        xor_values = nums[:]
        children = [set() for _ in range(n)]
        visited = [False] * n

        # Safely choose a root: prefer node with degree > 1, or fall back to node 0
        root = next((i for i in range(n) if len(graph[i]) > 1), 0)

        def dfs(node: int, parent: int) -> None:
            """
            DFS traversal to compute:
            - XOR of each subtree
            - Set of children (descendants) for each node

            Parameters:
                node (int): Current node.
                parent (int): Parent node to avoid revisiting.
            """
            visited[node] = True
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
                xor_values[node] ^= xor_values[neighbor]
                children[node].add(neighbor)
                children[node] |= children[neighbor]

        # Perform DFS to populate xor_values and children
        dfs(root, -1)

        result = sys.maxsize  # Initialize result to a large number

        # Try removing every pair of edges
        for i in range(len(edges)):
            for j in range(i):
                # Unpack edges
                a1, b1 = edges[i]
                a2, b2 = edges[j]

                # Normalize edges so child is the first node
                if b1 in children[a1]:
                    a1, b1 = b1, a1
                if b2 in children[a2]:
                    a2, b2 = b2, a2

                # Case 1: Edge2 inside Edge1's subtree
                if a2 in children[a1]:
                    x1 = xor_values[a2]
                    x2 = xor_values[a1] ^ xor_values[a2]
                    x3 = xor_values[root] ^ xor_values[a1]
                # Case 2: Edge1 inside Edge2's subtree
                elif a1 in children[a2]:
                    x1 = xor_values[a1]
                    x2 = xor_values[a2] ^ xor_values[a1]
                    x3 = xor_values[root] ^ xor_values[a2]
                # Case 3: Disjoint subtrees
                else:
                    x1 = xor_values[a1]
                    x2 = xor_values[a2]
                    x3 = xor_values[root] ^ xor_values[a1] ^ xor_values[a2]

                # Update result with minimal score
                result = min(result, max(x1, x2, x3) - min(x1, x2, x3))

        return result
