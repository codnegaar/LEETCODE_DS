'''
BS Leetcode 108 Convert Sorted Array to Binary Search Tree
 
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Example 1:
        Input: nums = [-10,-3,0,5,9]
        Output: [0,-3,9,-10,null,5]
        Explanation: [0,-10,5,null,-3,null,9] is also accepted

Example 2:
        Input: nums = [1,3]
        Output: [3,1]
        Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
         
Constraints:
        1 <= nums.length <= 104
        -104 <= nums[i] <= 104
        nums is sorted in a strictly increasing order.

'''
from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Converts a sorted array into a height-balanced binary search tree.
        
        Parameters:
        nums (List[int]): A sorted array of integers.
        
        Returns:
        Optional[TreeNode]: The root of the height-balanced BST.
        """
        def helpFunc(l: int, r: int) -> Optional[TreeNode]:
            """
            Recursive helper function to build the BST from the array indices.
            
            Parameters:
            l (int): Left boundary of the current subarray.
            r (int): Right boundary of the current subarray.
            
            Returns:
            Optional[TreeNode]: The root node of the subtree.
            """
            if l > r:  # Base case: invalid range
                return None
            
            # Find the middle index
            m = (l + r) // 2
            
            # Create the root node with the middle element
            root = TreeNode(nums[m])
            
            # Recursively construct the left subtree
            root.left = helpFunc(l, m - 1)
            
            # Recursively construct the right subtree
            root.right = helpFunc(m + 1, r)
            
            return root
        
        # Start the recursion with the full range
        return helpFunc(0, len(nums) - 1)

# Helper function to convert BST to a list for testing
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Converts a binary tree to a list using level-order traversal.
    """
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Unit tests
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    nums1 = [-10, -3, 0, 5, 9]
    bst1 = solution.sortedArrayToBST(nums1)
    print(tree_to_list(bst1))  # Expected: [0, -10, 5, None, -3, None, 9]

    nums2 = [1, 2, 3, 4, 5]
    bst2 = solution.sortedArrayToBST(nums2)
    print(tree_to_list(bst2))  # Expected: [3, 1, 4, None, 2, None, 5]

    nums3 = []
    bst3 = solution.sortedArrayToBST(nums3)
    print(tree_to_list(bst3))  # Expected: []

    nums4 = [1]
    bst4 = solution.sortedArrayToBST(nums4)
    print(tree_to_list(bst4))  # Expected: [1]

    nums5 = [1, 2]
    bst5 = solution.sortedArrayToBST(nums5)
    print(tree_to_list(bst5))  # Expected: [2, 1]
 
