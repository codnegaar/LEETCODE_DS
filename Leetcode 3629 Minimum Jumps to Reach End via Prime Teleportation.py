'''
Leetcode 3629 Minimum Jumps to Reach End via Prime Teleportation
 
You are given an integer array nums of length n.

You start at index 0, and your goal is to reach index n - 1.

From any index i, you may perform one of the following operations:

Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps required to reach index n - 1.

 

Example 1:
        Input: nums = [1,2,4,6]
        Output: 2
        Explanation:
        One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
Thus, the answer is 2.

Example 2:
        Input: nums = [2,3,4,7,9]        
        Output: 2        
                Explanation:    One optimal sequence of jumps is:
                Start at index i = 0. Take an adjacent step to index i = 1.
                At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
                Thus, the answer is 2.
Example 3:
        Input: nums = [4,6,5,8]
        Output: 3
        Explanation: Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.

Constraints:
        1 <= n == nums.length <= 105
        1 <= nums[i] <= 106

'''

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Function to find all prime factors of a number
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        gr = {}  # Map: prime factor → list of indices whose values are divisible by it
        for i in range(n):
            fac = prime_factors(arr[i])
            for ele in fac:
                if ele in gr:
                    gr[ele].append(i)     
                else:
                    gr[ele] = [i]         

        h = [[0, -0]]  # Min-heap with [distance, negative index] (negative for getting greater index)
        dis = [inf] * n
        dis[0] = 0        

        while h:
            val, node = heapq.heappop(h)  
            if node == -(n - 1):          
                return val
            node = -node             

            # Adjacent left move
            if node - 1 >= 0 and dis[node - 1] > val + 1:
                dis[node - 1] = val + 1
                heapq.heappush(h, [val + 1, -(node - 1)])

            # Adjacent right move
            if node + 1 < n and dis[node + 1] > val + 1:
                dis[node + 1] = val + 1
                heapq.heappush(h, [val + 1, -(node + 1)])

            # Prime teleportation move using prime factors of arr[node]
            if arr[node] in gr:
                for nei in gr[arr[node]]:
                    if dis[nei] > val + 1:
                        dis[nei] = val + 1
                        heapq.heappush(h, [val + 1, -nei])
