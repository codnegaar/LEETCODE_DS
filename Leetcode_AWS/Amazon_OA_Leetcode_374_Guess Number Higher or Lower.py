'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked. Every time you guess wrong, I will tell you whether
the number I picked is higher or lower than your guess. You call a pre-defined API int guess(int num), which returns three 
possible results:

   -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).
    
    Return the number that I picked.
    
Example 1:
   Input: n = 10, pick = 6
   Output: 6

'''

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1 , n
        
        while True:
            m = (l+r)//2
            
            result = guess(m)
            
            if result > 0:
                l = m + 1  
                
            elif result < 0:
                r = m - 1
            else:
                return m
'''
Second solution 
'''
 
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        m=(l+r)/2
        while r>=l:
            if guess(m)==0: return m
            if guess(m)==-1: 
                r=m-1
                m=(l+r)/2
            if guess(m)==1:
                l=m+1
                m=(l+r)/2
        
        return m;
'''
