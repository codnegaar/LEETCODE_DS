'''
Leetcode 1394 Find Lucky Integer in an Array

Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:
        Input: arr = [2,2,3,4]
        Output: 2
        Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
        Input: arr = [1,2,2,3,3,3]
        Output: 3
        Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
        Input: arr = [2,2,2,3,3]
        Output: -1
        Explanation: There are no lucky numbers in the array.
         
Constraints:
        1 <= arr.length <= 500
        1 <= arr[i] <= 500

'''
from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        Finds the largest lucky integer in the array.
        A lucky integer is one whose value is equal to its frequency in the array.

        Parameters:
        arr (List[int]): List of integers.

        Returns:
        int: The largest lucky integer if found, otherwise -1.
        """
        # Count the frequency of each number in the list
        frequency = Counter(arr)

        # Use a generator expression to find all numbers where value == frequency
        # Return the maximum of such values, or -1 if none found
        lucky_numbers = [num for num, freq in frequency.items() if num == freq]

        return max(lucky_numbers, default=-1)

