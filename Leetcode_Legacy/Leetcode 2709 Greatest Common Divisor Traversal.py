'''

Leetcode 2709 Greatest Common Divisor Traversal
 
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i 
and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.
Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.
Return true if it is possible to traverse between all such pairs of indices, or false otherwise. 

Example 1:
        Input: nums = [2,3,6]
        Output: true
        Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
        To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
        To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
        

Example 2:
        Input: nums = [3,9,5]
        Output: false
        Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.

Example 3:
        Input: nums = [4,3,12,8]
        Output: true
        Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
         
Constraints:
        1 <= nums.length <= 105
        1 <= nums[i] <= 105

'''

from typing import List
from math import isqrt, gcd

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        # Union-Find helper functions
        parent = list(range(len(nums)))
        rank = [0] * len(nums)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        # Connect components with common prime factors
        prime_to_index = {}
        for idx, num in enumerate(nums):
            for prime in range(2, isqrt(num) + 1):
                if num % prime == 0:
                    if prime in prime_to_index:
                        union(prime_to_index[prime], idx)
                    prime_to_index[prime] = idx
                    while num % prime == 0:
                        num //= prime
            if num > 1:  # num is prime
                if num in prime_to_index:
                    union(prime_to_index[num], idx)
                prime_to_index[num] = idx
        
        # Check if all numbers are connected
        first_parent = find(0)
        return all(find(i) == first_parent for i in range(len(nums)))

# Example Usage
sol = Solution()
print(sol.canTraverseAllPairs([6, 10, 15]))  # Expected: True
print(sol.canTraverseAllPairs([7, 11, 13]))  # Expected: False
print(sol.canTraverseAllPairs([8, 32, 24]))  # Expected: True


