'''

Leetcode 2530 Maximal Score After Applying K Operations

You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
In one operation:
        choose an index i such that 0 <= i < nums.length,
        increase your score by nums[i], and
        replace nums[i] with ceil(nums[i] / 3).
        Return the maximum possible score you can attain after applying exactly k operations.
The ceiling function ceil(val) is the least integer greater than or equal to val.

Example 1:
        Input: nums = [10,10,10,10,10], k = 5
        Output: 50
        Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

Example 2:
        Input: nums = [1,10,3,3,3], k = 3
        Output: 17
        Explanation: You can do the following operations:
        Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
        Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
        Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
        The final score is 10 + 4 + 3 = 17.
         

Constraints:
        1 <= nums.length, k <= 105
        1 <= nums[i] <= 109

'''

from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        # Convert the list to a max-heap by negating the elements (heapq is a min-heap by default)
        pq = [-x for x in nums]
        heapify(pq)

        score = 0
        
        # Loop for 'k' iterations
        for i in range(k):

            # Get the largest element (by negating the pop result)
            x = -heappop(pq)
            score += x
            
            # If the largest element is 1, no need to continue (rest elements will be 1s)
            if x == 1:
                
                # Add the remaining operations to the score since all will be 1
                score += (k - 1 - i)
                break
            
            # Push back the modified element (equivalent to ceil(x / 3))
            heappush(pq, -((x + 2) // 3))
        
        return score
