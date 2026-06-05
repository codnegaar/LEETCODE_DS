'''

Leetcode 3753 Total Waviness of Numbers in Range II


You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
 

Example 1:
Input: num1 = 120, num2 = 130
Output: 3
Explanation:
In the range [120, 130]:
        120: middle digit 2 is a peak, waviness = 1.
        121: middle digit 2 is a peak, waviness = 1.
        130: middle digit 3 is a peak, waviness = 1.
        All other numbers in the range have a waviness of 0.
        Thus, total waviness is 1 + 1 + 1 = 3.

Example 2:
        Input: num1 = 198, num2 = 202        
        Output: 3
        
        Explanation:        
        In the range [198, 202]:        
                198: middle digit 9 is a peak, waviness = 1.
                201: middle digit 0 is a valley, waviness = 1.
                202: middle digit 0 is a valley, waviness = 1.
                All other numbers in the range have a waviness of 0.
                Thus, total waviness is 1 + 1 + 1 = 3.

Example 3:        
        Input: num1 = 4848, num2 = 4848        
        Output: 2        
        Explanation:        
        Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.
        
         

Constraints:

1 <= num1 <= num2 <= 1015​​​​​​​

'''
class Solution:

    def solve(self, n: int) -> int:

        if n <= 0:
            return 0

        s = str(n)
        memo = {}

        def dfs(pos, tight, started, prev2, prev1):

            if pos == len(s):
                return (0, 1)  # (waviness, count)

            key = (pos, tight, started, prev2, prev1)

            if key in memo:
                return memo[key]

            total_waviness = 0
            total_cnt = 0

            limit = int(s[pos]) if tight else 9

            for d in range(limit + 1):

                next_tight = tight and (d == limit)

                if not started and d == 0:

                    child_waviness, child_cnt = dfs(pos + 1,next_tight,False,10,10)

                    total_waviness += child_waviness
                    total_cnt += child_cnt

                else:

                    add = 0

                    if not started:

                        n_prev2 = 10
                        n_prev1 = d

                    else:

                        if prev2 != 10:

                            peak = (prev1 > prev2 and prev1 > d)
                            valley = (prev1 < prev2 and prev1 < d)

                            if peak or valley:
                                add = 1

                        n_prev2 = prev1
                        n_prev1 = d

                    child_waviness, child_cnt = dfs(pos + 1,next_tight,True,n_prev2,n_prev1)

                    total_waviness += (child_waviness +add * child_cnt)
                    total_cnt += child_cnt

            memo[key] = (total_waviness, total_cnt)
            return memo[key]

        return dfs(0, True, False, 10, 10)[0]

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2) - self.solve(num1 - 1)
