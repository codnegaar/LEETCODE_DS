'''
Leetcode 2940 Find Building Where Alice and Bob Can Meet
 
You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.
If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].
You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.
Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

Example 1:
        Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
        Output: [2,5,-1,5,2]
        Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
        In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
        In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
        In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
        In the fifth query, Alice and Bob are already in the same building.  
        For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
        For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

Example 2:
        Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
        Output: [7,6,-1,4,6]
        Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
        In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
        In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
        In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
        In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
        For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
        For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
           
Constraints:
        1 <= heights.length <= 5 * 104
        1 <= heights[i] <= 109
        1 <= queries.length <= 5 * 104
        queries[i] = [ai, bi]
        0 <= ai, bi <= heights.length - 1
'''

from typing import List

class Solution:
    """
    This class provides a method to find the leftmost building that is taller than any of the buildings
    in the specified range of queries.
    
    Methods:
    leftmostBuildingQueries(heights: List[int], queries: List[List[int]]) -> List[int]:
        Finds the leftmost building taller than all buildings in the range [l, r] for each query.
    """

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        
        # st[i][j] will store the maximum height in the range [i, i + 2^j]
        st = [[0] * 20 for _ in range(n)]
        
        # Log[i] will store the largest power of 2 that is <= i
        Log = [-1] * (n + 1)
        
        # Precompute logs to optimize range queries
        for i in range(1, n + 1):
            Log[i] = Log[i >> 1] + 1
        
        # Initialize the sparse table for the base case (intervals of length 1)
        for i in range(n):
            st[i][0] = heights[i]
        
        # Build the sparse table for larger intervals
        for i in range(1, 20):
            for j in range(n):
                if j + (1 << i) <= n:
                    st[j][i] = max(st[j][i - 1], st[j + (1 << (i - 1))][i - 1])

        # Helper function to get the maximum height in the range [l, r]
        def Ask(l, r):
            k = Log[r - l + 1]
            return max(st[l][k], st[r - (1 << k) + 1][k])
        
        # Process each query to find the leftmost building taller than all in the range
        res = []
        for l, r in queries:
            # Ensure l <= r
            if l > r:
                l, r = r, l
            
            # If both indices are the same, the answer is the same index
            if l == r:
                res.append(l)
                continue
            
            # If building at r is taller than at l, answer is r
            if heights[r] > heights[l]:
                res.append(r)
                continue
            
            # Find the maximum height in the range [l, r]
            max_height = max(heights[r], heights[l])
            left, right = r + 1, n
            
            # Binary search to find the leftmost building taller than max_height
            while left < right:
                mid = (left + right) // 2
                if Ask(r + 1, mid) > max_height:
                    right = mid
                else:
                    left = mid + 1
            
            # If no building is taller, append -1, else append the index of the building
            res.append(left if left != n else -1)
        
        return res

