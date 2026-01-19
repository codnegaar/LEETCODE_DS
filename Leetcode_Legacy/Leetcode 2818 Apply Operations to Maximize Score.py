'''
Leetcode 2818 Apply Operations to Maximize Score

You are given an array nums of n positive integers and an integer k.
Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:
Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
Multiply your score by x.
Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.
The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.
Return the maximum possible score after applying at most k operations.
Since the answer may be large, return it modulo 109 + 7.

Example 1:        
        Input: nums = [8,3,9,3,8], k = 2
        Output: 81
        Explanation: To get a score of 81, we can apply the following operations:
        - Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
        - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
        It can be proven that 81 is the highest score one can obtain.

Example 2:        
        Input: nums = [19,12,14,6,10,18], k = 3
        Output: 4788
        Explanation: To get a score of 4788, we can apply the following operations: 
        - Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
        - Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
        - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
        It can be proven that 4788 is the highest score one can obtain.
         

Constraints:
        1 <= nums.length == n <= 105
        1 <= nums[i] <= 105
        1 <= k <= min(n * (n + 1) / 2, 109)

'''


from typing import List

class Solution:
    MOD = 10**9 + 7

    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        Calculates the maximum score after performing at most k operations.

        Parameters:
        - nums (List[int]): List of positive integers.
        - k (int): Number of operations allowed.

        Returns:
        - int: Maximum possible score modulo 10^9 + 7.
        """
        n = len(nums)
        max_num = max(nums) + 1

        # Precompute number of distinct prime factors (primeScore) using sieve
        prime = [True] * max_num
        prime[0] = prime[1] = False
        primeScore = [0] * max_num

        for i in range(2, max_num):
            if prime[i]:
                for j in range(i, max_num, i):
                    primeScore[j] += 1
                    prime[j] = False  # Mark as not prime

        # Monotonic stack to find Next Greater Element (based on primeScore)
        next_greater = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and primeScore[nums[i]] >= primeScore[nums[stack[-1]]]:
                stack.pop()
            next_greater[i] = stack[-1] if stack else n
            stack.append(i)

        # Monotonic stack to find Previous Greater or Equal Element (based on primeScore)
        prev_greater_equal = [-1] * n
        stack = []
        for i in range(n):
            while stack and primeScore[nums[i]] > primeScore[nums[stack[-1]]]:
                stack.pop()
            prev_greater_equal[i] = stack[-1] if stack else -1
            stack.append(i)

        # Sort nums with indices in descending order of value
        indexed_nums = sorted([[nums[i], i] for i in range(n)], reverse=True)

        result = 1
        for num, idx in indexed_nums:
            # Calculate how many times num can be used
            left = idx - prev_greater_equal[idx]
            right = next_greater[idx] - idx
            operations = min(left * right, k)

            # Multiply result by num^operations % MOD
            result = (result * self.fast_pow(num, operations)) % self.MOD
            k -= operations
            if k == 0:
                break

        return result

    def fast_pow(self, base: int, exp: int) -> int:
        """
        Computes (base ^ exp) % MOD using fast exponentiation.

        Parameters:
        - base (int): Base number.
        - exp (int): Exponent.

        Returns:
        - int: Result of (base ^ exp) % MOD
        """
        result = 1
        base %= self.MOD
        while exp:
            if exp % 2:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            exp //= 2
        return result
