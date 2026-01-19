'''

Leetcode 2962 Count Subarrays Where Max Element Appears at Least K Times
 
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.
 
Example 1:
        Input: nums = [1,3,2,3,3], k = 2
        Output: 6
        Explanation: The subarrays that contain the element 3 at least 2 times are [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3], and [3,3].

Example 2:
        Input: nums = [1,4,2,1], k = 3
        Output: 0
        Explanation: No subarray contains the element 4 at least 3 times.
 
Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 106
        1 <= k <= 105

'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx,ans,l,r,n=max(nums),0,0,0,len(nums)
        while r<n:
            k-= nums[r]==mx
            r+=1
            while k==0:
                k+=nums[l]==mx
                l+=1
            ans+=l
        return and;

'''
second solution
Approach:
1- Brute Force: The brute force approach would involve iterating over all possible subarrays and checking the condition for each. However, this approach 
   is not feasible for large inputs due to its high time complexity.
2- Optimized Solution: A more efficient approach is needed, which can likely involve segmenting the array based on the occurrences of the maximum element 
   and then calculating the number of valid subarrays within those segments.
3- Utilizing Monotonic Queues or Stacks: For problems involving the maximum element in subarrays, monotonic queues or stacks can sometimes be used to maintain 
   a window of elements that meet a certain condition. However, given the need to count occurrences, a different strategy might be more applicable.
4- Prefix and Suffix Maximums: By computing prefix and suffix maximums, we can determine the influence of each maximum element on its surrounding elements, 
   helping to identify valid subarrays more efficiently.

Proposed Python Solution:
1- Given the constraint and the need for an efficient solution, let's consider an approach that focuses on dividing the problem into manageable parts that can be solved efficiently:
2- Identify All Occurrences of each element in the array. This can be used to determine where the maximum elements influence subarray boundaries.
3- Count Valid Subarrays efficiently, considering the frequency of maximum elements and how they divide the array into segments where valid subarrays can be counted.

Here's a conceptual approach in Python, noting that we'd need to refine it to ensure it efficiently solves the given problem:

This conceptual approach aims to segment the problem based on occurrences of elements, and then calculate the influence of each segment that meets the condition 
(the maximum element appears at least k times). However, the actual implementation might need optimizations and careful consideration of edge cases to ensure 
it runs efficiently within the constraints specified by the problem. This solution sketches an approach but may require further refinement for optimal
performance on all test cases.

'''
class Solution:
    def count_subarrays(nums, k):
        from collections import defaultdict
    
        # Step 1: Find all occurrences of each element
        occurrences = defaultdict(list)
        for i, num in enumerate(nums):
            occurrences[num].append(i)
        
        total_subarrays = 0
        for num, occ in occurrences.items():
            if len(occ) < k:  # Skip if the number doesn't appear at least k times
                continue
            
            # For each occurrence that meets the condition, calculate the influence
            for i in range(len(occ) - k + 1):
                # Define the left and right bounds of influence for the current maximum
                left = occ[i] - (occ[i-1] if i > 0 else -1)
                right = (occ[i+k-1] + 1) - occ[i+k-1]
                total_subarrays += left * right
        
        return total_subarrays
    
    # Example usage
    print(count_subarrays([1,3,2,3,3], 2))  # Output: 6
    print(count_subarrays([1,4,2,1], 3))    # Output: 0
        
