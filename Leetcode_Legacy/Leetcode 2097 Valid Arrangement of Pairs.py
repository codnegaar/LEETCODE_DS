'''

Leetcode 2097 Valid Arrangement of Pairs

You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.
Return any valid arrangement of pairs.
Note: The inputs will be generated such that there exists a valid arrangement of pairs.

Example 1:
        Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
        Output: [[11,9],[9,4],[4,5],[5,1]]
        Explanation:
        This is a valid arrangement since endi-1 always equals starti.
        end0 = 9 == 9 = start1 
        end1 = 4 == 4 = start2
        end2 = 5 == 5 = start3

Example 2:
        Input: pairs = [[1,3],[3,2],[2,1]]
        Output: [[1,3],[3,2],[2,1]]
        Explanation:
        This is a valid arrangement since endi-1 always equals starti.
        end0 = 3 == 3 = start1
        end1 = 2 == 2 = start2
        The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.

Example 3:
        Input: pairs = [[1,2],[1,3],[2,1]]
        Output: [[1,2],[2,1],[1,3]]
        Explanation:
                This is a valid arrangement since endi-1 always equals starti.
                end0 = 2 == 2 = start1
                end1 = 1 == 1 = start2
 
Constraints:
        1 <= pairs.length <= 105
        pairs[i].length == 2
        0 <= starti, endi <= 109
        starti != endi
        No two pairs are exactly the same.
        There exists a valid arrangement of pairs.

'''

from collections import defaultdict, deque

class Solution:
    def validArrangement(self, pairs):
        """
        Finds a valid arrangement of pairs such that each pair follows from the previous one.

        The function constructs a directed graph from the pairs, then finds an Eulerian path
        that visits each pair exactly once.

        Parameters:
        pairs (List[List[int]]): A list of pairs where each pair represents an edge in a directed graph.
        
        Returns:
        List[List[int]]: The valid arrangement of pairs that forms an Eulerian path.
        """
        
        # Create a graph using a dictionary of deques, and track in-degrees and out-degrees
        graph = defaultdict(deque)
        inDegree, outDegree = defaultdict(int), defaultdict(int)

        # Build the graph and compute the in-degrees and out-degrees
        for start, end in pairs:
            graph[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        # Find the start node: It should have one more outgoing edge than incoming edges
        startNode = pairs[0][0]  # Default to the first node of the first pair
        for node in graph:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break

        # Path to store the Eulerian path
        path = []

        def dfs(node):
            """
            Depth First Search to visit all edges starting from the current node.
            It adds the visited nodes to the path in reverse order.
            """
            while graph[node]:
                nextNode = graph[node].popleft()  # Take the next node to visit
                dfs(nextNode)
            path.append(node)  # Add the node to the path once all its edges are visited

        # Perform DFS starting from the determined start node
        dfs(startNode)

        # Reverse the path to get the correct order of nodes
        path.reverse()

        # Construct the result by pairing consecutive nodes in the path
        return [[path[i], path[i + 1]] for i in range(len(path) - 1)]
