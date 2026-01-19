'''
Leetcode 1395 Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:
Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
        Input: rating = [2,5,3,4,1]
        Output: 3
        Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:
        Input: rating = [2,1,3]
        Output: 0
        Explanation: We can't form any team given the conditions.

Example 3:
        Input: rating = [1,2,3,4]
        Output: 4 

Constraints:
        n == rating.length
        3 <= n <= 1000
        1 <= rating[i] <= 105
        All the integers in rating are unique.

'''

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        
        teams = 0
        
        # Loop over each element to count valid teams
        for i in range(1, n - 1):
            left_smaller = left_larger = right_smaller = right_larger = 0
            
            # Count how many elements are smaller or larger on the left side of rating[i]
            for j in range(i):
                if rating[j] < rating[i]:
                    left_smaller += 1
                elif rating[j] > rating[i]:
                    left_larger += 1
            
            # Count how many elements are smaller or larger on the right side of rating[i]
            for k in range(i + 1, n):
                if rating[k] < rating[i]:
                    right_smaller += 1
                elif rating[k] > rating[i]:
                    right_larger += 1
            
            # Calculate teams in ascending and descending order
            teams += left_smaller * right_larger  # Ascending team
            teams += left_larger * right_smaller  # Descending team
        
        return teams
