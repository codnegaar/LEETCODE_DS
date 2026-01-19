'''
Leetcode 1028 Recover a Tree From Preorder Traversal
 
We run a preorder depth-first search (DFS) on the root of a binary tree.
At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node. 
If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
If a node has only one child, that child is guaranteed to be the left child.
Given the output traversal of this traversal, recover the tree and return its root. 

Example 1:
        Input: traversal = "1-2--3--4-5--6--7"
        Output: [1,2,5,3,4,6,7]

Example 2:
        Input: traversal = "1-2--3---4-5--6---7"
        Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:
        Input: traversal = "1-401--349---90--88"
        Output: [1,401,null,349,88,90]
 
Constraints:
        The number of nodes in the original tree is in the range [1, 1000].
        1 <= Node.val <= 109
'''

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        i, n = 0, len(traversal)
        stack = []
        
        while i < n:
            level, num = 0, ""

            # Count dashes to determine depth level
            while i < n and traversal[i] == '-':
                level += 1
                i += 1

            # Read the number (node value)
            while i < n and traversal[i] != '-':
                num += traversal[i]
                i += 1

            node = TreeNode(int(num))

            # Adjust stack to maintain correct tree structure
            while len(stack) > level:
                stack.pop()

            # Attach node to its parent
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0]  # Root of the tree

