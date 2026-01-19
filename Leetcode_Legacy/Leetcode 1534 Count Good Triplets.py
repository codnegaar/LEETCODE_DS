'''
Leetcode 1534 Count Good Triplets

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.
Return the number of good triplets.

Example 1:
        Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
        Output: 4
        Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

Example 2:
        Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
        Output: 0
        Explanation: No triplet satisfies all conditions.
         

Constraints:        
        3 <= arr.length <= 100
        0 <= arr[i] <= 1000
        0 <= a, b, c <= 1000

'''

from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Count the number of good triplets in the array.
        
        A triplet (i, j, k) is good if:
            0 <= i < j < k < len(arr), and
            |arr[i] - arr[j]| <= a,
            |arr[j] - arr[k]| <= b,
            |arr[i] - arr[k]| <= c

        Parameters:
        arr (List[int]): The input array of integers.
        a (int): Maximum allowed absolute difference between arr[i] and arr[j].
        b (int): Maximum allowed absolute difference between arr[j] and arr[k].
        c (int): Maximum allowed absolute difference between arr[i] and arr[k].

        Returns:
        int: Total number of good triplets satisfying the given conditions.
        """
        count = 0
        n = len(arr)

        # Iterate through all triplets (i, j, k) where i < j < k
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        # Check the remaining two conditions
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
        return count
