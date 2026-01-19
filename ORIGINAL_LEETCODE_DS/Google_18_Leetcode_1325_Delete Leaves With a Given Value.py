'''

Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, if its parent node becomes a leaf node
and has the value target, it should also be deleted (you need to continue doing that until you cannot). 

Example 1:
  Input: root = [1,2,3,2,null,2,4], target = 2
  Output: [1,null,3,null,4]
  Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
  After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:
  Input: root = [1,3,3,3,2], target = 3
  Output: [1,3,null,null,2]

Example 3:
  Input: root = [1,2,null,2,null,2], target = 2
  Output: [1]
  Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

Constraints:
  The number of nodes in the tree is in the range [1, 3000].
  1 <= Node.val, target <= 1000
  
***************************************** Solution *************************************
Runtime complexity: O(n)
Space complexity: O(1)
 
First, we have to find the key in the linked list. WeΓÇÖll keep two pointers, current and previous, as we iterate the linked list.
If the key is found in the linked list, then the current pointer would be pointing to the node containing the key to be deleted.
The previous should be pointing to the node before the key node. This can be done in a linear scan and we can simply update current
and previous pointers as we iterate through the linked list.


class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes
 
  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]
 
  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def popper(vertex):
            if vertex == None:
                return 
            
            vertex.left = popper(vertex.left)
            vertex.right = popper(vertex.right)
            
            if not vertex.left  and not vertex.right and vertex.val == target:
                return None
            return vertex

        return popper(root)
      
      
      
 
