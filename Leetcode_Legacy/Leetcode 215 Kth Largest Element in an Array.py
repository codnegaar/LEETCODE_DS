'''

Leetcode 215 Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.


Example 1:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5
        
Example 2:
        Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
        Output: 4
        
Constraints:
        1 <= k <= nums.length <= 105
        -104 <= nums[i] <= 104
        
'''
class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    minHeap = []

    for num in nums:
      heapq.heappush(minHeap, num)
      if len(minHeap) > k:
        heapq.heappop(minHeap)

    return minHeap[0]


# Second solution
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find the k-th largest element in an unsorted array using a Min-Heap.

        Parameters:
        nums (List[int]): List of integers.
        k (int): The k-th largest element to find.

        Returns:
        int: The k-th largest element.
        """
        # Build a Min-Heap of size k
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate over the remaining elements
        for num in nums[k:]:
            # If the current number is greater than the smallest in the heap, replace it
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        # The root of the heap is the k-th largest element
        return min_heap[0]

# Example of implementation
nums = [3, 2, 1, 5, 6, 4]
k = 2
solution = Solution()
result = solution.findKthLargest(nums, k)
print(f"The {k}-th largest element is: {result}")  # Expected output: 5

