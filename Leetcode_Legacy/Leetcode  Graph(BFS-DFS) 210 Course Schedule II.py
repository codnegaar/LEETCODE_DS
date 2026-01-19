'''
Leetcode 210 Course Schedule II
 
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.


'''

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    ans = []
    graph = [[] for _ in range(numCourses)]
    inDegree = [0] * numCourses
    q = collections.deque()

    # Build graph
    for v, u in prerequisites:
      graph[u].append(v)
      inDegree[v] += 1

    # Topology
    for i, degree in enumerate(inDegree):
      if degree == 0:
        q.append(i)

    while q:
      u = q.popleft()
      ans.append(u)
      for v in graph[u]:
        inDegree[v] -= 1
        if inDegree[v] == 0:
          q.append(v)

    return ans if len(ans) == numCourses else []


# Second Solution
from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Determines the order of courses to finish all given the prerequisites.

        Parameters:
        - numCourses (int): Total number of courses labeled from 0 to numCourses-1.
        - prerequisites (List[List[int]]): List of prerequisite pairs where [a, b]
          means course `a` depends on course `b`.

        Returns:
        - List[int]: A list of course numbers in the order they should be taken.
          If it is impossible to complete all courses, return an empty list.
        """
        # Step 1: Create adjacency list and initialize data structures
        adj = [[] for _ in range(numCourses)]  # Adjacency list for graph representation
        indeg = [0] * numCourses  # Array to store in-degrees of nodes (courses)
        result = []  # To store the topological order
        queue = deque()  # Queue for BFS traversal

        # Step 2: Build the adjacency list and in-degree array
        for course, prereq in prerequisites:
            adj[prereq].append(course)  # Add edge prereq -> course
            indeg[course] += 1         # Increment in-degree of course

        # Step 3: Add all courses with 0 in-degree to the queue
        for course in range(numCourses):
            if indeg[course] == 0:
                queue.append(course)

        # Step 4: Process nodes with BFS
        while queue:
            course = queue.popleft()  # Remove a course with 0 in-degree
            result.append(course)     # Add it to the result (topological order)

            # Reduce in-degree of neighboring courses
            for neighbor in adj[course]:
                indeg[neighbor] -= 1  # Reduce in-degree by 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)  # If in-degree becomes 0, add to queue

        # Step 5: Check if topological sorting is possible
        if len(result) == numCourses:
            return result  # All courses can be completed
        else:
            return []  # Cycle detected or not all courses can be completed


# solution 2
import collections
from typing import List
import string

class Solution:
    """
    Class to solve the word ladder problem using a breadth-first search (BFS) approach.

    Methods:
        ladderLength: Finds the shortest transformation sequence from `beginWord` to `endWord`.
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str], alphabet: str = string.ascii_lowercase) -> int:
        """
        Find the length of the shortest transformation sequence from `beginWord` to `endWord`.

        A valid transformation changes only one letter at a time, and all intermediate words must 
        be present in the `wordList`.

        Parameters:
        - beginWord (str): The starting word of the sequence.
        - endWord (str): The target word of the sequence.
        - wordList (List[str]): The list of allowed words for transformation.
        - alphabet (str): The set of characters allowed for transformation (default: lowercase English letters).

        Returns:
        - int: The length of the shortest transformation sequence, or 0 if no sequence exists.
        """
        # Convert wordList to a set for O(1) lookups
        wordSet = set(wordList)
        
        # If the endWord is not in the wordList, transformation is impossible
        if endWord not in wordSet:
            return 0

        # BFS queue initialized with the beginWord
        queue = collections.deque([beginWord])
        # Track the transformation steps (start at 1 for beginWord)
        steps = 1  

        # Process until the queue is empty
        while queue:
            # Iterate over all words in the current BFS level
            for _ in range(len(queue)):
                currentWord = queue.popleft()
                
                # Modify each character in the word
                for i in range(len(currentWord)):
                    # Save the original character
                    original_char = currentWord[i]

                    # Try all possible characters from the alphabet
                    for char in alphabet:
                        # Skip if the character is the same
                        if char == original_char:
                            continue
                        
                        # Create the new word by replacing the character
                        newWord = currentWord[:i] + char + currentWord[i+1:]
                        
                        # If the endWord is reached, return steps + 1
                        if newWord == endWord:
                            return steps + 1
                        
                        # If the new word exists in the wordSet, process it
                        if newWord in wordSet:
                            queue.append(newWord)       # Add to the BFS queue
                            wordSet.remove(newWord)     # Remove to prevent revisiting

            # Increment the step count after processing the current level
            steps += 1

        # Return 0 if no valid transformation is found
        return 0

# Unit Test
def test_ladderLength():
    solution = Solution()

    # Test cases
    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert solution.ladderLength("a", "c", ["a", "b", "c"]) == 2
    assert solution.ladderLength("abc", "def", ["abc", "abd", "abf", "dbf", "dff", "def"]) == 4
    assert solution.ladderLength("aaa", "ccc", ["aab", "abb", "bbb", "bbc", "bcc", "ccc"]) == 6

    print("All tests passed.")

# Example usage
if __name__ == "__main__":
    test_ladderLength()

# Python Documentation Reference:
# - `collections.deque`: https://docs.python.org/3/library/collections.html#collections.deque
# - `string.ascii_lowercase`: https://docs.python.org/3/library/string.html#string.ascii_lowercase

# Key changes made:
# 1. Added detailed docstrings for the method and class.
# 2. Improved readability with better formatting and comments.
# 3. Optimized the BFS loop with a queue and removal of visited words to prevent duplicates.
# 4. Provided a comprehensive unit test suite.
# 5. Added examples and references to Python documentation.

