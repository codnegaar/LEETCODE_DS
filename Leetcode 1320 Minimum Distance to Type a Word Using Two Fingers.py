'''
Leetcode 1320 Minimum Distance to Type a Word Using Two Fingers


You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.
For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
Given the string word, return the minimum total distance to type such string using only two fingers.
The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.
Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

Example 1:
        Input: word = "CAKE"
        Output: 3
        Explanation: Using two fingers, one optimal way to type "CAKE" is: 
        Finger 1 on letter 'C' -> cost = 0 
        Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
        Finger 2 on letter 'K' -> cost = 0 
        Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
        Total distance = 3

Example 2:
        Input: word = "HAPPY"
        Output: 6
        Explanation: Using two fingers, one optimal way to type "HAPPY" is:
        Finger 1 on letter 'H' -> cost = 0
        Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
        Finger 2 on letter 'P' -> cost = 0
        Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
        Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
        Total distance = 6
         

Constraints:
        2 <= word.length <= 300
        word consists of uppercase English letters.

'''
from functools import lru_cache
class Solution:
    def minimumDistance(self, A):
        
        @lru_cache(maxsize=None)
        def get_distance(current_pos, next_pos):
            if current_pos == -1: return 0
            return abs(current_pos // 6 - next_pos // 6) + abs(current_pos % 6 - next_pos % 6)
        
        @lru_cache(maxsize=None)
        def to_num(c):
            return ord(c) - ord('A')

        # key: (i,j) i is the position of the first finger, j is the positino of the second finger
        dp = {(to_num(A[0]), -1): 0} # base case, -1 means the second finger is free
        for n in [to_num(c) for c in A[1:]]:
            new_dp = {}
            for (f1, f2), d in dp.items():
                new_dp[n, f2] = min(new_dp.get((n, f2), math.inf), d + get_distance(f1, n))
                new_dp[f1, n] = min(new_dp.get((f1, n), math.inf), d + get_distance(f2, n))
            dp = new_dp
            
        return min(dp.values())
		
