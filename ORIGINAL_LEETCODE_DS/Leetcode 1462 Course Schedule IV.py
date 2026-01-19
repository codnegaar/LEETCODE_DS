'''
Leetcode 1462 Course Schedule IV
 
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.
For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.
You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:
        Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
        Output: [false,true]
        Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
        Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:
        Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
        Output: [false,false]
        Explanation: There are no prerequisites, and each course is independent.

Example 3:
        Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
        Output: [true,true]
         

Constraints:
        2 <= numCourses <= 100
        0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
        prerequisites[i].length == 2
        0 <= ai, bi <= numCourses - 1
        ai != bi
        All the pairs [ai, bi] are unique.
        The prerequisites graph has no cycles.
        1 <= queries.length <= 104
        0 <= ui, vi <= numCourses - 1
        ui != vi
'''
from collections import deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Determines if the prerequisites for each query are valid in the given course graph.
        
        Parameters:
        - numCourses (int): Total number of courses.
        - prerequisites (List[List[int]]): A list of pairs where each pair [a, b] indicates
          that course `a` is a prerequisite for course `b`.
        - queries (List[List[int]]): A list of pairs where each pair [x, y] checks if `x`
          is a prerequisite for `y`.
        
        Returns:
        - List[bool]: A list of boolean values indicating whether each query is valid.
        """

        # Step 1: Initialize graph, reachability matrix, and indegree array
        graph = [[] for _ in range(numCourses)]  # Adjacency list for the graph
        reachable = [[0] * numCourses for _ in range(numCourses)]  # Reachability matrix
        indegree = [0] * numCourses  # Array to track indegree of each course

        # Step 2: Build the graph and update indegree based on prerequisites
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            indegree[pre[1]] += 1

        # Step 3: Initialize queue with courses that have no prerequisites (indegree = 0)
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        # Step 4: Perform BFS to calculate reachability matrix
        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                # Update reachability matrix for direct and indirect prerequisites
                reachable[node][neighbor] = 1
                for i in range(numCourses):
                    if reachable[i][node]:  # If `i` can reach `node`, it can also reach `neighbor`
                        reachable[i][neighbor] = 1

                # Reduce indegree and add neighbor to queue if its indegree becomes 0
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Step 5: Process queries using the reachability matrix
        return [bool(reachable[query[0]][query[1]]) for query in queries]


# Test the Solution class
if __name__ == "__main__":
    solution = Solution()
    numCourses = 4
    prerequisites = [[0, 1], [1, 2], [2, 3]]
    queries = [[0, 3], [1, 3], [3, 0], [2, 0]]
    print("Query Results:", solution.checkIfPrerequisite(numCourses, prerequisites, queries))


