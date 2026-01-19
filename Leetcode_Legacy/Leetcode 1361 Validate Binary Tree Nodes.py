'''

Leetcode 1361 Validate Binary Tree Nodes

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
Note that the nodes have no values and that we only use the node numbers in this problem. 

Example 1:
        Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
        Output: true

Example 2:
        Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
        Output: false

Example 3:
        Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
        Output: false
 
Constraints:
        n == leftChild.length == rightChild.length
        1 <= n <= 104
        -1 <= leftChild[i], rightChild[i] <= n - 1

'''

from queue import Queue
class Solution:
    def isBinaryTreeValid(self, root: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = [False] * len(leftChild)  # Tracks visited nodes
        nodeQueue = Queue()  # Queue for BFS traversal
        nodeQueue.put(root)
        visited[root] = True

        while not nodeQueue.empty():
            current = nodeQueue.get()

            # Check left child
            if leftChild[current] != -1:
                if visited[leftChild[current]]:  # Check for cycle
                    return False

                nodeQueue.put(leftChild[current])
                visited[leftChild[current]] = True  # Mark left child as visited

            # Check right child
            if rightChild[current] != -1:
                if visited[rightChild[current]]:  # Check for cycle
                    return False

                nodeQueue.put(rightChild[current])
                visited[rightChild[current]] = True  # Mark right child as visited

        # Check if there are multiple components
        for visit in visited:
            if not visit:
                return False

        return True  # All nodes form a valid binary tree

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        childCount = [False] * n  # Tracks child count for each node

        # Update child count based on leftChild
        for child in leftChild:
            # Check if node has child
            if child != -1:
                childCount[child] = True  # Mark left child as having a parent

        # Update child count based on rightChild
        for child in rightChild:
            # Check if node has child
            if child != -1:
                if childCount[child]:  # Check if the right child already has a parent
                    return False

                childCount[child] = True  # Mark right child as having a parent

        root = -1  # Root node
        for i in range(n):
            if not childCount[i]:
                if root == -1:
                    root = i  # Set root node if not assigned
                else:
                    return False  # Multiple roots found, not a valid binary tree

        if root == -1:
            return False  # No root found, not a valid binary tree

        return self.isBinaryTreeValid(root, leftChild, rightChild)  # Check if the tree is valid


# second solution

