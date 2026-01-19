'''
Leetcode 2593 Find Score of an Array After Marking All Elements

You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:
        Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
        Add the value of the chosen integer to score.
        Mark the chosen element and its two adjacent elements if they exist.
        Repeat until all the array elements are marked.
        Return the score you get after applying the above algorithm.

Example 1:
        Input: nums = [2,1,3,4,5,2]
        Output: 7
        Explanation: We mark the elements as follows:
        - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
        - 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
        - 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
        Our score is 1 + 2 + 4 = 7.

Example 2:
        Input: nums = [2,3,5,1,3,2]
        Output: 5
        Explanation: We mark the elements as follows:
        - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
        - 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
        - 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
        Our score is 1 + 2 + 2 = 5.
 
Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 106
'''

class Solution:
    def findScore(self, nums):
        """
        Calculate the score of an array based on the given rules:
        - Add the smallest available value to the score.
        - Mark the chosen value and its neighbors as used (visited).

        Parameters:
        nums (List[int]): The input list of integers.

        Returns:
        int: The calculated score.
        """
        # Track the visited indices
        visited = [False] * len(nums)
        
        # Pair each number with its index and sort the array (ensures smallest first)
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        
        # Initialize the score
        score = 0

        # Traverse the sorted list
        for val, idx in indexed_nums:
            if not visited[idx]:  # If the current index is not visited
                score += val  # Add the value to the score
                # Mark current and adjacent indices as visited
                visited[idx] = True
                if idx > 0:
                    visited[idx - 1] = True
                if idx < len(nums) - 1:
                    visited[idx + 1] = True

        return score



