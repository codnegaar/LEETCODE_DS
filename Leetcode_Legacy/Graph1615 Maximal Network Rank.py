'''
Graph 1615 Maximal Network Rank

There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.
The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

 
Example 1:
        Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
        Output: 4
        Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

Example 2:
        Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
        Output: 5
        Explanation: There are 5 roads that are connected to cities 1 or 2.

Example 3:
        Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
        Output: 5
        Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
 

Constraints:
        2 <= n <= 100
        0 <= roads.length <= n * (n - 1) / 2
        roads[i].length == 2
        0 <= ai, bi <= n-1
        ai != bi
        Each pair of cities has at most one road connecting them.

'''

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(set)
        for a, b in roads:
            g[a].add(b)
            g[b].add(a)
        ans = 0
        for a in range(n):
            for b in range(a + 1, n):
                if (t := len(g[a]) + len(g[b]) - (a in g[b])) > ans:
                    ans = t
        return and

# Solution 2
from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
        This function takes an integer array 'nums' and an integer 'maximumBit', and returns a list 
        of integers that represents the maximum XOR value obtainable by choosing a k in range(0, 2^maximumBit).
        
        Parameters:
            nums (List[int]): List of integers
            maximumBit (int): The number of bits for the maximum value k can have
        
        Returns:
            List[int]: List of integers representing the maximum XOR obtainable at each step
        """
        
        # Initialize the XOR of all elements and a mask for maximum bit constraint
        current_xor = 0
        mask = (1 << maximumBit) - 1  # This creates a mask like '111...1' for maximum possible k with 'maximumBit' bits
        
        # Calculate the XOR of all elements in nums once
        for num in nums:
            current_xor ^= num

        # Generate the answer by reversing through the list and applying the mask to maximize XOR
        ans = []
        for num in reversed(nums):
            ans.append(current_xor ^ mask)  # Maximize XOR for the current prefix
            current_xor ^= num  # Remove the current number to adjust prefix XOR

        return ans


