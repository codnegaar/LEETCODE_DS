'''
Leetcode 2560 House Robber IV

There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.
You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.
Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

Example 1:
        Input: nums = [2,3,5,9], k = 2
        Output: 5

Explanation: 
        There are three ways to rob at least 2 houses:
        - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
        - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
        - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
        Therefore, we return min(5, 9, 9) = 5.

Example 2:
        Input: nums = [2,7,9,3,1], k = 2
        Output: 2
        Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
         
Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 109
        1 <= k <= (nums.length + 1)/2

'''
from typing import List

class Solution:
    """
    A class to determine the minimum capability required to pick `k` houses 
    from a given list of house values, following the constraint that no two 
    adjacent houses can be picked.
    """

    def minCapability(self, nums: List[int], k: int) -> int:
        """
        Uses binary search to find the minimum capability required to pick `k` 
        houses while ensuring no two adjacent houses are selected.

        Parameters:
        nums (List[int]): A list of house values.
        k (int): The number of houses to be picked.

        Returns:
        int: The minimum capability required.
        """

        def canPick(limit: int) -> bool:
            """
            Determines if `k` houses can be picked without selecting adjacent ones, 
            given a maximum allowed value of `limit`.

            Parameters:
            limit (int): The maximum house value that can be picked.

            Returns:
            bool: True if at least `k` houses can be picked, otherwise False.
            """
            count = 0  # Count of houses picked
            i = 0  # Iterator for `nums`
            n = len(nums)  # Length of house list

            while i < n:
                if nums[i] <= limit:
                    count += 1  # Pick this house
                    i += 2  # Skip next house (to maintain non-adjacency)
                else:
                    i += 1  # Move to the next house
            
            return count >= k  # Ensure we can pick at least `k` houses

        # Binary search for the minimum valid capability
        left, right = min(nums), max(nums)  # Possible range for capability

        while left < right:
            mid = (left + right) // 2  # Middle value
            if canPick(mid):
                right = mid  # Try lower capability
            else:
                left = mid + 1  # Increase capability

        return left  # The minimum valid capability
