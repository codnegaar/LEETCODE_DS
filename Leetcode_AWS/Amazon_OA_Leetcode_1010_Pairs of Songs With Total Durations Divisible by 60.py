'''
Leetcode 1010: Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration of time[i] seconds.
Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, 
we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
 

Example 1:

  Input: time = [30,20,150,100,40]
  Output: 3
  
  Explanation: Three pairs have a total duration divisible by 60:
      (time[0] = 30, time[2] = 150): total duration 180
      (time[1] = 20, time[3] = 100): total duration 120
      (time[1] = 20, time[4] = 40): total duration 60
      
Example 2:
        Input: time = [60,60,60]
        Output: 3
        Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 
Constraints:
          1 <= time.length <= 6 * 104
          1 <= time[i] <= 500

'''

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
         
        hash = {}
        pairs = 0

        for num in time:
            remainder = num % 60
            
            if remainder == 0:
                if 0 in hash:
                    pairs  += hash[0]
                
            elif (60 - remainder) in hash:
                pairs += hash[60 - remainder]

            if remainder in hash:
                hash[remainder] += 1
            else:
                hash[remainder] = 1
        return pairs
       
       
# Solution II

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        pairs = 0
        current = [0] * 60
        
        for t in time:
            t %= 60
            pairs += current[(60-t) % 60]
            current[t] += 1
        return pairs
       
       
       
