'''
Leetcode 1855 Maximum Distance Between a Pair of Values
 
You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.
A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.
Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.
An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length. 

Example 1:
        Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
        Output: 2
        Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
        The maximum distance is 2 with pair (2,4).

Example 2:
        Input: nums1 = [2,2,2], nums2 = [10,10,1]
        Output: 1
        Explanation: The valid pairs are (0,0), (0,1), and (1,1).
        The maximum distance is 1 with pair (0,1).

Example 3:
        Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
        Output: 2
        Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
        The maximum distance is 2 with pair (2,4).
 
Constraints:
        1 <= nums1.length, nums2.length <= 105
        1 <= nums1[i], nums2[j] <= 105
        Both nums1 and nums2 are non-increasing.
'''
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        rev = nums2[::-1]

        def binary(target) -> int:
            low, high = 0, n-1
            while low <= high:
                mid = (low+high)//2
                if rev[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return low 

        maxdis = 0
        for i, num in enumerate(nums1):
            j = binary(num)
            j = n-j
            if 0 <= j-1 < n and i <= j-1 and num <= nums2[j-1]:
                maxdis = max(maxdis, j-1-i)
        return maxdis 


