'''
Leetcode BS 378 Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).


Example 1:
        Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
        Output: 13
        Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
        Input: matrix = [[-5]], k = 1
        Output: -5
 

Constraints:
        n == matrix.length == matrix[i].length
        1 <= n <= 300
        -109 <= matrix[i][j] <= 109
        All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
        1 <= k <= n2

'''
class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    minHeap = []  # (matrix[i][j], i, j)

    i = 0
    while i < k and i < len(matrix):
      heapq.heappush(minHeap, (matrix[i][0], i, 0))
      i += 1

    while k > 1:
      k -= 1
      _, i, j = heapq.heappop(minHeap)
      if j + 1 < len(matrix[0]):
        heapq.heappush(minHeap, (matrix[i][j + 1], i, j + 1))

    return minHeap[0][0]
