'''
Leetcode 2392 Build a Matrix With Conditions

You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.
You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.
The matrix should also satisfy the following conditions:
The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.

Example 1:
        Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
        Output: [[3,0,0],[0,0,1],[0,2,0]]
        Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
        The row conditions are the following:
        - Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
        - Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
        The column conditions are the following:
        - Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
        - Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
        Note that there may be multiple correct answers.

Example 2:
        Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
        Output: []
        Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
        No matrix can satisfy all the conditions, so we return the empty matrix.
         
Constraints:
        2 <= k <= 400
        1 <= rowConditions.length, colConditions.length <= 104
        rowConditions[i].length == colConditions[i].length == 2
        1 <= abovei, belowi, lefti, righti <= k
        abovei != belowi
        lefti != righti
'''

from collections import defaultdict, deque

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        # Build adjacency lists for row and column conditions
        rowGraph = defaultdict(list)
        colGraph = defaultdict(list)

        for x in rowConditions:
            rowGraph[x[0]].append(x[1])
        for x in colConditions:
            colGraph[x[0]].append(x[1])

        # Function to perform topological sort and detect cycles
        def topologicalSort(graph):
            stack = deque()
            visited = set()
            in_progress = set()
            
            def dfs(node):
                if node in in_progress:  # Cycle detected
                    return False
                if node in visited:
                    return True  # Already processed this node, skip
                
                visited.add(node)
                in_progress.add(node)
                
                for neighbor in graph[node]:
                    if not dfs(neighbor):
                        return False  # Cycle detected further down
                
                in_progress.remove(node)
                stack.appendleft(node)  # Add node to the topological sort result
                return True
            
            # Attempt to visit all nodes 1 through k
            for i in range(1, k + 1):
                if i not in visited:
                    if not dfs(i):
                        return []  # Return empty list if a cycle is detected
            
            return list(stack)

        # Get topological orders for both row and column graphs
        rowOrder = topologicalSort(rowGraph)
        colOrder = topologicalSort(colGraph)

        # If a cycle is detected in either, return empty matrix
        if not rowOrder or not colOrder:
            return []

        # Create a mapping from number to its row index in the topological order
        rowMapping = {num: i for i, num in enumerate(rowOrder)}
        
        # Build the result matrix
        matrix = [[0] * k for _ in range(k)]
        for colIdx, num in enumerate(colOrder):
            rowIdx = rowMapping[num]
            matrix[rowIdx][colIdx] = num
        
        return matrix
