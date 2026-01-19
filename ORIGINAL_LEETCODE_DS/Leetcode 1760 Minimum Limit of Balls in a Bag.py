'''
Leetcode 1760 Minimum Limit of Balls in a Bag

You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.
You can perform the following operation at most maxOperations times:
Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.
Return the minimum possible penalty after performing the operations.


Example 1:
        Input: nums = [9], maxOperations = 2
        Output: 3
        Explanation: 
        - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
        - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
        The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

Example 2:
        Input: nums = [2,4,8,2], maxOperations = 4
        Output: 2
        Explanation:
        - Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
        - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
        - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
        - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
        The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.
         

Constraints:
        1 <= nums.length <= 105
        1 <= maxOperations, nums[i] <= 109

'''
from typing import List

class Solution:
    def minimumSize(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum possible size of the largest bag after performing at most k operations.

        Parameters:
        nums (List[int]): A list of integers representing the size of the bags.
        k (int): The maximum number of operations allowed to split the bags.

        Returns:
        int: The minimum size of the largest bag.
        """
        # Define the search space: 1 (minimum size) to the largest element in nums (max size)
        left, right = 1, max(nums)
        
        # Perform binary search
        while left < right:
            mid = (left + right) // 2  # Middle point
            # Count the operations needed to ensure all bags are <= mid
            operations = sum((num - 1) // mid for num in nums)
            
            if operations <= k:  # If operations are within the allowed limit
                right = mid  # Try to minimize the largest size
            else:
                left = mid + 1  # Increase the size limit
            
        return left

# Unit Tests
def test_minimum_size():
    solution = Solution()
    
    # Example Test Cases
    nums1, k1 = [9], 2
    assert solution.minimumSize(nums1, k1) == 3, f"Test 1 failed: {solution.minimumSize(nums1, k1)}"
    
    nums2, k2 = [2, 4, 8, 2], 4
    assert solution.minimumSize(nums2, k2) == 2, f"Test 2 failed: {solution.minimumSize(nums2, k2)}"
    
    nums3, k3 = [1, 2, 3, 4], 0
    assert solution.minimumSize(nums3, k3) == 4, f"Test 3 failed: {solution.minimumSize(nums3, k3)}"
    
    nums4, k4 = [7, 17], 2
    assert solution.minimumSize(nums4, k4) == 7, f"Test 4 failed: {solution.minimumSize(nums4, k4)}"
    
    print("All tests passed!")

# Run the tests
test_minimum_size()
