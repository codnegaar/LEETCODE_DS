'''
Leetcode  DFS 508 Most Frequent Subtree Sum


Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

Example 1:
        Input: root = [5,2,-3]
        Output: [2,-3,4]
        
Example 2:
        Input: root = [5,2,-5]
        Output: [2] 

Constraints:
        The number of nodes in the tree is in the range [1, 104].
        -105 <= Node.val <= 105
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []

    count = collections.Counter()

    def dfs(root: Optional[TreeNode]) -> int:
      if not root:
        return 0

      summ = root.val + dfs(root.left) + dfs(root.right)
      count[summ] += 1
      return summ

    dfs(root)
    maxFreq = max(count.values())
    return [summ for summ in count if count[summ] == maxFreq]

        
