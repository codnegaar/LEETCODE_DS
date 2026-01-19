'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.
        
Example 2:
        Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.
Example 3:
        Input: nums = [0,0,0]
        Output: [[0,0,0]]
        Explanation: The only possible triplet sums up to 0.
Constraints:
        3 <= nums.length <= 3000
        -105 <= nums[i] <= 105
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


# Second solution

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array which give the sum of zero.

        Args:
        - nums (List[int]): List of integers.

        Returns:
        - List[List[int]]: A list of unique triplets such that the sum of each triplet is zero.
        """
        # Sort the list to facilitate two-pointer approach
        nums.sort()
        n = len(nums)
        result = []

        # Iterate over the sorted array
        for i in range(n):
            # If current number is greater than zero, further triplets will not sum to zero
            if nums[i] > 0:
                break
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two-pointer approach for the remainder of the array
            left, right = i + 1, n - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                # Check if the current triplet sums to zero
                if total_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate elements to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                # If the sum is less than zero, move the left pointer to the right
                elif total_sum < 0:
                    left += 1
                # If the sum is greater than zero, move the right pointer to the left
                else:
                    right -= 1

        return result

        
