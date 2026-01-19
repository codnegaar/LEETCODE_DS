'''
Leetcode 1865 Finding Pairs With a Certain Sum

You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:
Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:
        FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
        void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
        int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.

Example 1:
        Input
        ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
        [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
        Output
        [null, 8, null, 2, 1, null, null, 11]
        Explanation
                FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
                findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
                findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
                findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
                findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
                findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
                findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
                findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
 
Constraints:
        1 <= nums1.length <= 1000
        1 <= nums2.length <= 105
        1 <= nums1[i] <= 109
        1 <= nums2[i] <= 105
        0 <= index < nums2.length
        1 <= val <= 105
        1 <= tot <= 109
        At most 1000 calls are made to add and count each.

'''
from collections import Counter

class FindSumPairs:
    """
    Class to support adding values to an index in nums2 and counting the number of pairs
    (one from nums1 and one from nums2) that sum up to a given total.

    Attributes:
        nums1 (List[int]): First list of integers (read-only).
        nums2 (List[int]): Second list of integers (mutable).
        counter2 (Counter): Frequency map of elements in nums2 for efficient counting.
    """

    def __init__(self, nums1, nums2):
        """
        Initialize with two lists.

        Args:
            nums1 (List[int]): First list of integers.
            nums2 (List[int]): Second list of integers.
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)  # O(n) frequency map for nums2

    def add(self, index, val):
        """
        Add val to nums2[index] and update the frequency map.

        Args:
            index (int): Index in nums2 to update.
            val (int): Value to add.
        """
        old_val = self.nums2[index]
        new_val = old_val + val

        # Update nums2 and frequency map
        self.nums2[index] = new_val
        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]
        self.counter2[new_val] += 1

    def count(self, tot):
        """
        Count the number of pairs (x from nums1, y from nums2) such that x + y == tot.

        Args:
            tot (int): Target sum to check.

        Returns:
            int: Number of valid pairs.
        """
        result = 0
        for x in self.nums1:
            complement = tot - x
            result += self.counter2.get(complement, 0)
        return result



