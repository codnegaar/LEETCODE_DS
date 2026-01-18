'''

Leetcode 427 Construct Quad Tree

Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:
If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.
If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:
        You don't need to read this section for solving the problem. This is only if you want to understand the output format here. 
        The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.
        It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].
        If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

Example 1:
        Input: grid = [[0,1],[1,0]]
        Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
        Explanation: The explanation of this example is shown below:
        Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

Example 2:
        Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
        Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
        Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
        The topLeft, bottomLeft and bottomRight each has the same value.
        The topRight have different values so we divide it into 4 sub-grids where each has the same value.
        Explanation is shown in the photo below:

Constraints:
        n == grid.length == grid[i].length
        n == 2x where 0 <= x <= 6

'''
from typing import List, Optional

class Node:
    """
    Represents a node in a quadtree.

    Attributes:
        val (bool): The value of the node (True for 1, False for 0).
        isLeaf (bool): Whether the node is a leaf node.
        topLeft (Optional[Node]): Top-left child node.
        topRight (Optional[Node]): Top-right child node.
        bottomLeft (Optional[Node]): Bottom-left child node.
        bottomRight (Optional[Node]): Bottom-right child node.
    """
    def __init__(self, val: bool, isLeaf: bool, 
                 topLeft: Optional['Node'] = None, 
                 topRight: Optional['Node'] = None, 
                 bottomLeft: Optional['Node'] = None, 
                 bottomRight: Optional['Node'] = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """
    Constructs a quadtree from a given grid.
    """
    def construct(self, grid: List[List[int]]) -> Node:
        """
        Constructs a quadtree from a 2D grid.

        Args:
            grid (List[List[int]]): A 2D grid of integers (0 or 1).

        Returns:
            Node: The root node of the constructed quadtree.
        """
        return self._construct_helper(grid, 0, 0, len(grid))

    def _construct_helper(self, grid: List[List[int]], row: int, col: int, size: int) -> Node:
        """
        Helper function to recursively build the quadtree.

        Args:
            grid (List[List[int]]): A 2D grid of integers.
            row (int): Starting row index of the current quadrant.
            col (int): Starting column index of the current quadrant.
            size (int): Size of the current quadrant.

        Returns:
            Node: The quadtree node representing the current quadrant.
        """
        # Base case: If all values in the current quadrant are the same, create a leaf node
        if self._is_uniform(grid, row, col, size):
            return Node(grid[row][col] == 1, True)

        # Recursively divide the grid into 4 quadrants
        half_size = size // 2
        return Node(
            val=True,  # Placeholder value for non-leaf nodes
            isLeaf=False,
            topLeft=self._construct_helper(grid, row, col, half_size),
            topRight=self._construct_helper(grid, row, col + half_size, half_size),
            bottomLeft=self._construct_helper(grid, row + half_size, col, half_size),
            bottomRight=self._construct_helper(grid, row + half_size, col + half_size, half_size)
        )

    def _is_uniform(self, grid: List[List[int]], row: int, col: int, size: int) -> bool:
        """
        Checks if all values in the current quadrant are the same.

        Args:
            grid (List[List[int]]): A 2D grid of integers.
            row (int): Starting row index of the current quadrant.
            col (int): Starting column index of the current quadrant.
            size (int): Size of the current quadrant.

        Returns:
            bool: True if all values are the same, False otherwise.
        """
        first_value = grid[row][col]
        for i in range(row, row + size):
            for j in range(col, col + size):
                if grid[i][j] != first_value:
                    return False
        return True



