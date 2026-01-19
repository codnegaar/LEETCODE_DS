'''
Leetcode 1502 Can Make Arithmetic Progression From Sequence

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
 
Example 1:
        Input: arr = [3,5,1]
        Output: true
        Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences of 2 and -2 respectively, between each consecutive element.

Example 2:
        Input: arr = [1,2,4]
        Output: false
        Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
      
Constraints:
        2 <= arr.length <= 1000
        -106 <= arr[i] <= 106
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:        
        arr.sort()  
        diff = arr[1] - arr[0]        
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True

# Solution 2
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:        
        length = len(arr)
        min_val = min(arr)
        max_val = max(arr)
        diff = (max_val - min_val) / (length - 1)
        for i in range(length):
            expected = min_val + i * diff
            if expected not in arr:
                return False
        return True
