'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
        Input: nums = [1,2,3,1]
        Output: true
Example 2:
        Input: nums = [1,2,3,4]
        Output: false
Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         return len(nums) != len(set(nums))

# second solution
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer list `nums`, this function checks if there are any duplicate values in the list.
        
        Parameters:
        - nums (list[int]): A list of integers.
        
        Returns:
        - bool: True if any value appears at least twice in the array, False otherwise.
        """
        # Use a set to track the unique numbers encountered in the list
        seen = set()

        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the set, it means a duplicate is found
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        
        # No duplicates found after checking all numbers
        return False
