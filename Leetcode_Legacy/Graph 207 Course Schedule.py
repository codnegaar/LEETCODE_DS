'''
Leetcode (Detecting Cycles in a Graph) 207 Course Schedule
 
You have to take a total of numCourses courses, labeled from 0 to numCourses - 1. You are given an array of 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have first to take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:
        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
        Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0. So it is possible.

Example 2:
        Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: false
        Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
        1 <= numCourses <= 2000
        0 <= prerequisites.length <= 5000
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        All the pairs prerequisites[i] are unique.


'''

from enum import Enum

class State(Enum):
  kInit = 0
  kVisiting = 1
  kVisited = 2

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    state = [State.kInit] * numCourses

    for a, b in prerequisites:
      graph[b].append(a)

    def hasCycle(u: int) -> bool:
      if state[u] == State.kVisiting:
        return True
      if state[u] == State.kVisited:
        return False

      state[u] = State.kVisiting
      if any(hasCycle(v) for v in graph[u]):
        return True
      state[u] = State.kVisited

      return False

    return not any(hasCycle(i) for i in range(numCourses))


# second solution:

from enum import Enum
from typing import List

class State(Enum):
    kInit = 0
    kVisiting = 1
    kVisited = 2

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it is possible to finish all courses given the prerequisites.
        
        Args:
            numCourses (int): The total number of courses.
            prerequisites (List[List[int]]): A list of prerequisite pairs where 
                                             each pair [a, b] indicates that course b 
                                             must be taken before course a.
        
        Returns:
            bool: True if it is possible to complete all courses, False otherwise.
        """
        # Create a graph represented as an adjacency list for the courses
        graph = [[] for _ in range(numCourses)]
        # Create an array to store the state of each course (initial, visiting, visited)
        state = [State.kInit] * numCourses

        # Build the graph from prerequisites list
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Function to check if there is a cycle starting from a given course
        def hasCycle(course: int) -> bool:
            if state[course] == State.kVisiting:
                return True  # A cycle is detected
            if state[course] == State.kVisited:
                return False  # Course has already been processed
            
            # Mark the course as currently being visited
            state[course] = State.kVisiting
            # Recursively visit all the adjacent courses
            for next_course in graph[course]:
                if hasCycle(next_course):
                    return True  # Cycle detected

            # Mark the course as completely processed
            state[course] = State.kVisited
            return False

        # Check each course for cycles
        for course in range(numCourses):
            if hasCycle(course):
                return False

        # If no cycle is detected for any course, return True
        return True

# Example usage:
# solution = Solution()
# print(solution.canFinish(2, [[1, 0]]))  # Should return True
# print(solution.canFinish(2, [[1, 0], [0, 1]]))  # Should return False


# Second solution
from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be finished given the prerequisites.

        Parameters:
        - numCourses: int: Total number of courses labeled from 0 to numCourses-1.
        - prerequisites: List[List[int]]: A list of prerequisite pairs where [a, b]
          means course `a` requires course `b` to be taken first.

        Returns:
        - bool: True if all courses can be finished, False otherwise.
        """

        # Step 1: Build the adjacency list for the graph.
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Step 2: Define states for the nodes (courses).
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(course: int) -> bool:
            """
            Perform Depth First Search to detect cycles.

            Parameters:
            - course: int: Current course being visited.

            Returns:
            - bool: True if no cycle is detected, False otherwise.
            """
            if states[course] == VISITED:
                return True  # Course has already been processed, no cycle here.
            if states[course] == VISITING:
                return False  # Cycle detected.

            # Mark the course as being visited.
            states[course] = VISITING

            # Visit all neighbors (dependent courses).
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False  # Cycle detected in the neighbor.

            # Mark the course as fully visited.
            states[course] = VISITED
            return True

        # Step 3: Check all courses for cycles.
        for course in range(numCourses):
            if states[course] == UNVISITED:
                if not dfs(course):
                    return False

        return True

# Unit Tests
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print("Test Case 1:", solution.canFinish(numCourses1, prerequisites1))  # Expected: True

    # Example 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print("Test Case 2:", solution.canFinish(numCourses2, prerequisites2))  # Expected: False

    # Example 3: No prerequisites
    numCourses3 = 3
    prerequisites3 = []
    print("Test Case 3:", solution.canFinish(numCourses3, prerequisites3))  # Expected: True

    # Example 4: Complex dependencies with no cycle
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 1], [3, 2]]
    print("Test Case 4:", solution.canFinish(numCourses4, prerequisites4))  # Expected: True

    # Example 5: Complex dependencies with a cycle
    numCourses5 = 4
    prerequisites5 = [[1, 0], [2, 1], [0, 2]]
    print("Test Case 5:", solution.canFinish(numCourses5, prerequisites5))  # Expected: False


