'''
133 Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2,
and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


Example 1:
        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]
        Explanation: There are 4 nodes in the graph.
        1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
        3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
        Input: adjList = [[]]
        Output: [[]]
        Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
        Input: adjList = []
        Output: []
        Explanation: This an empty graph, it does not have any nodes.
 

Constraints:
        The number of nodes in the graph is in the range [0, 100].
        1 <= Node.val <= 100
        Node.val is unique for each node.
        There are no repeated edges and no self-loops in the graph.
        The Graph is connected and all nodes can be visited starting from the given node.

'''


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
      return None

    q = collections.deque([node])
    map = {node: Node(node.val)}

    while q:
      u = q.popleft()
      for v in u.neighbors:
        if v not in map:
          map[v] = Node(v.val)
          q.append(v)
        map[u].neighbors.append(map[v])

    return map[node]

# Second solution

"""
Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

This module provides a solution to clone a graph using DFS.
"""

from typing import Optional, Dict

class Node:
    """Class to represent a Node in an undirected graph."""
    def __init__(self, val=0, neighbors=None):
        self.val = val  # Value of the node
        self.neighbors = neighbors if neighbors is not None else []  # List of neighbors

class Solution:
    """
    Solution class to provide a method to clone an undirected graph.
    
    Methods:
        cloneGraph(node): Clones an undirected graph using DFS.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clones an undirected graph using DFS.

        Args:
            node (Optional[Node]): The input graph node to clone.

        Returns:
            Optional[Node]: The cloned graph node or None if input is None.
        """
        if not node:
            return None  # Return None if the input graph is empty

        seen: Dict[int, Node] = {}  # A dictionary to store cloned nodes

        def dfs(curr_node: 'Node') -> 'Node':
            """
            Performs a DFS to clone the graph.
            
            Args:
                curr_node (Node): Current node being visited.
                
            Returns:
                Node: Cloned node corresponding to the current node.
            """
            if curr_node.val in seen:
                # Return the already cloned node if it exists
                return seen[curr_node.val]
            
            # Create a copy of the current node
            clone = Node(curr_node.val)
            seen[curr_node.val] = clone  # Store the cloned node in the dictionary
            
            # Recursively clone the neighbors
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone  # Return the cloned node

        return dfs(node)  # Start DFS from the input node

# Unit Test
def test_clone_graph():
    """
    Unit test for the cloneGraph function.
    """
    # Create a sample graph: Node 1 connected to 2 and 4, Node 2 connected to 3, etc.
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()
    cloned_graph = solution.cloneGraph(node1)

    # Verify the structure of the cloned graph
    assert cloned_graph is not node1
    assert cloned_graph.val == 1
    assert len(cloned_graph.neighbors) == 2
    assert cloned_graph.neighbors[0].val == 2
    assert cloned_graph.neighbors[1].val == 4
    print("All tests passed!")

if __name__ == "__main__":
    test_clone_graph()

"""
Changes:
1. Optimized DFS by avoiding redundant checks in the recursive calls.
2. Improved readability by adding docstrings and comments for each step.
3. Added type hints for better clarity and maintainability.
4. Added a unit test to validate the solution with an example graph.
5. Included an implementation example and test coverage for better usability.
6. Reference to Python documentation: https://docs.python.org/3/library/typing.html for type hints.
"""

