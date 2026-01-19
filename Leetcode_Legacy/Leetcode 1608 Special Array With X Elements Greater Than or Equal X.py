'''
Leetcode 1608 Special Array With X Elements Greater Than or Equal X
 
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are 
exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Example 1:
        Input: nums = [3,5]
        Output: 2
        Explanation: There are 2 values (3 and 5) which are greater than or equal to 2.

Example 2:
        Input: nums = [0,0]
        Output: -1
        Explanation: No numbers fit the criteria for x.
                If x = 0, there should be 0 numbers >= x, but there are 2.
                If x = 1, there should be 1 number >= x, but there are 0.
                If x = 2, there should be 2 numbers >= x, but there are 0.
                x cannot be greater since there are only 2 numbers in nums.

Example 3:
        Input: nums = [0,4,3,0,4]
        Output: 3
        Explanation: 3 values are greater than or equal to 3.
         
Constraints:
        1 <= nums.length <= 100
        0 <= nums[i] <= 1000

'''


class Solution:
    def specialArray(self, nums: list[int]) -> int:
      
        """
        This method determines if there is an integer x such that there are exactly x elements in
        the array that are greater than or equal to x. The function sorts the array and uses binary
        search to efficiently count how many elements meet the condition for each possible x.
        
        :param nums: List of integers.
        :return: The special number x if it exists, otherwise -1.
        """
      
        # Sort the array to use binary search effectively
        nums.sort()
        n = len(nums)
        
        def find_number_of_nums(cur_num: int) -> int:
          
            """
            A helper function using binary search to find the number of elements in the sorted
            list 'nums' that are greater than or equal to 'cur_num'.
            
            :param cur_num: The current number to compare the elements in the list against.
            :return: Number of elements greater than or equal to cur_num.
            """
            left, right = 0, n - 1

            # Initialize to n (out of bounds), indicating no valid index found yet.
            first_index = n  

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= cur_num:
                    first_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            # Count of elements >= cur_num
            return n - first_index  

        # Check each number from 1 to n if it can be the special number
        for candidate_number in range(1, n + 1):
            if candidate_number == find_number_of_nums(candidate_number):
                return candidate_number
              
        # Return -1 if no special number is found
        return -1  

