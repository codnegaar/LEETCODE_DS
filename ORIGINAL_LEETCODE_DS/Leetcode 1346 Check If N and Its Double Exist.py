'''
Leetcode 1346 Check If N and Its Double Exist
 
Given an array arr of integers, check if there exist two indices i and j such that :
        i != j
        0 <= i, j < arr.length
        arr[i] == 2 * arr[j]
 
Example 1:
        Input: arr = [10,2,5,3]
        Output: true
        Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
        Input: arr = [3,1,7,11]
        Output: false
        Explanation: There is no i and j that satisfy the conditions.
     
Constraints:
      2 <= arr.length <= 500
      -103 <= arr[i] <= 103



'''

from typing import List

class Solution:
    """
    A solution to check if there exist two numbers in an array such that one
    is double the other.
    """

    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Checks if there exists two indices i and j such that:
          - i != j
          - arr[i] == 2 * arr[j]
        
        Args:
            arr (List[int]): A list of integers.

        Returns:
            bool: True if such a pair exists, otherwise False.

        Examples:
            >>> Solution().checkIfExist([10, 2, 5, 3])
            True
            >>> Solution().checkIfExist([3, 1, 7, 11])
            False
            >>> Solution().checkIfExist([0, 0])
            True
        """
        # A set to store previously seen numbers
        lookup = set()

        # Iterate through each number in the array
        for x in arr:
            # Check if the current number's double exists in the set
            # or if the current number is even and its half exists in the set
            if 2 * x in lookup or (x % 2 == 0 and x // 2 in lookup):
                return True
            # Add the current number to the set for future checks
            lookup.add(x)

        # If no such pair is found, return False
        return False
