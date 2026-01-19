'''

Leetcode 2179 Count Good Triplets in an Array
 
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. 
In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, 
then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.
Return the total number of good triplets. 

Example 1:
        Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
        Output: 1
        Explanation: 
        There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
        Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.

Example 2:
        Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
        Output: 4
        Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
 

Constraints:
        n == nums1.length == nums2.length
        3 <= n <= 105
        0 <= nums1[i], nums2[i] <= n - 1
        nums1 and nums2 are permutations of [0, 1, ..., n - 1].
'''

from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Counts the number of good triplets (i, j, k) where i < j < k
        and the order of elements is the same in nums1 and nums2.
        """

        n = len(nums1)

        # Map value -> index in nums2
        pos_in_nums2 = [0] * n
        for i, val in enumerate(nums2):
            pos_in_nums2[val] = i

        # Map nums1 values to their positions in nums2
        mapped = [pos_in_nums2[val] for val in nums1]

        # Binary Indexed Tree (Fenwick Tree)
        class BIT:
            def __init__(self, size):
                self.tree = [0] * (size + 2)  # extra space for 1-based indexing

            def update(self, index, value):
                index += 1
                while index < len(self.tree):
                    self.tree[index] += value
                    index += index & -index

            def query(self, index):
                index += 1
                result = 0
                while index > 0:
                    result += self.tree[index]
                    index -= index & -index
                return result

        # Count how many numbers are smaller before and greater after
        bit = BIT(n)
        left_smaller = [0] * n
        right_greater = [0] * n

        # Count smaller to the left
        for i in range(n):
            left_smaller[i] = bit.query(mapped[i] - 1)
            bit.update(mapped[i], 1)

        # Reset BIT for right-to-left scan
        bit = BIT(n)

        # Count greater to the right
        for i in reversed(range(n)):
            right_greater[i] = bit.query(n - 1) - bit.query(mapped[i])
            bit.update(mapped[i], 1)

        # Total good triplets
        return sum(left_smaller[i] * right_greater[i] for i in range(n))

 
