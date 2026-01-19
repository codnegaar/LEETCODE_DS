'''

Leetcode 2196 Create Binary Tree From Descriptions

You are given a 2D integer array of descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,    
        If isLefti == 1, then childi is the left child of parenti.
        If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.
The test cases will be generated such that the binary tree is valid.

Example 1:
        Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
        Output: [50,20,80,15,17,19]
        Explanation: The root node is the node with value 50 since it has no parent.
        The resulting binary tree is shown in the diagram.
        
Example 2:
        Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
        Output: [1,2,null,null,3,4]
        Explanation: The root node is the node with value 1 since it has no parent.
        The resulting binary tree is shown in the diagram.
 
Constraints:
        1 <= descriptions.length <= 104
        descriptions[i].length == 3
        1 <= parenti, childi <= 105
        0 <= isLefti <= 1
        The binary tree described by descriptions is valid.

'''


from typing import List, Optional, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def construct_tree(node_val: int) -> TreeNode:
            new_node = TreeNode(node_val)
            if node_val in children_hashmap:
                left_child, right_child = children_hashmap[node_val]
                if left_child is not None:
                    new_node.left = construct_tree(left_child)
                if right_child is not None:
                    new_node.right = construct_tree(right_child)
            return new_node

        children_set = set()
        children_hashmap: Dict[int, List[Optional[int]]] = {}

        # Populate the children_hashmap and children_set
        for parent, child, isleft in descriptions:
            if parent not in children_hashmap:
                children_hashmap[parent] = [None, None]  # Initialize left and right children as None
            children_set.add(child)
            target = 0 if isleft else 1
            children_hashmap[parent][target] = child

        # Find the root node (a node that is not a child of any other node)
        root_val = next(parent for parent in children_hashmap if parent not in children_set)

        # Construct the tree starting from the root node
        return construct_tree(root_val)

'''


Explanation:
1- Type Hints and TreeNode Class:

Added type hints to the method signatures for better readability.
Added the TreeNode class definition for completeness.
construct_tree Function:

Simplified the construct_tree function by directly unpacking left_child and right_child from children_hashmap[node_val].
Populating the children_hashmap and children_set:

Created children_hashmap to map each parent to its left and right children.
Created children_set to keep track of all child nodes.
Finding the Root Node:

Used a generator expression to find the root node efficiently. The root node is a node that is not present in children_set.
Constructing the Tree:

Started the tree construction from the root node using the construct_tree function.


'''
