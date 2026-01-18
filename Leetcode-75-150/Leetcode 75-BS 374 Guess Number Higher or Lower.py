'''
Leetcode 75-BS 374 Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
        
       -1: Your guess is higher than the number I picked (i.e. num > pick).
        1: Your guess is lower than the number I picked (i.e. num < pick).
        0: your guess is equal to the number I picked (i.e. num == pick).
        Return the number that I picked.

 

Example 1:
        Input: n = 10, pick = 6
        Output: 
        
Example 2:
        Input: n = 1, pick = 1
        Output: 1
        
Example 3:
        Input: n = 2, pick = 1
        Output: 1
 
Constraints:
        1 <= n <= 231 - 1
        1 <= pick <= n

'''
class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 0
        higher = n
        
        while lower <= higher:
            
            mid = (lower + higher) // 2
            pick = guess(mid)
            
            if pick == 0:
                return mid
            elif pick == 1:
                lower = mid + 1
            else:
                higher = mid - 1

# secon solution

class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            m=(l+r)>>1
            if guess(m)==0:
                return m
            elif guess(m)==-1:
                r=m-1
            else:
                l=m+1
        
