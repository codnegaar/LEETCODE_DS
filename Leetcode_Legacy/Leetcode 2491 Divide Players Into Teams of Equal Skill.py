'''
Leetcode 2491 Divide Players Into Teams of Equal Skill

You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. 
Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
The chemistry of a team is equal to the product of the skills of the players on that team.
Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the 
players into teams such that the total skill of each team is equal.

Example 1:
        Input: skill = [3,2,5,1,3,4]
        Output: 22
        Explanation: 
                Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
                The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
                
Example 2:
        Input: skill = [3,4]
        Output: 12
        Explanation: 
        The two players form a team with a total skill of 7.
        The chemistry of the team is 3 * 4 = 12.
        
Example 3:
        Input: skill = [1,1,2,3]
        Output: -1
        Explanation: 
        There is no way to divide the players into teams such that the total skill of each team is equal. 

Constraints:
        2 <= skill.length <= 105
        skill.length is even.
        1 <= skill[i] <= 1000
'''
from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array
        skill.sort()
        
        n = len(skill)
        if n % 2 != 0:
            return -1  # Odd number of players, cannot be paired
        
        total_skill_per_pair = skill[0] + skill[-1]  # Required skill sum for each pair
        total_chemistry = 0

        # Step 2: Use two pointers to form pairs and calculate chemistry
        for i in range(n // 2):
            left_player = skill[i]
            right_player = skill[n - i - 1]
            
            # Check if the current pair's skill sum matches the required total_skill_per_pair
            if left_player + right_player != total_skill_per_pair:
                return -1  # Invalid configuration, return -1
            
            # Calculate the chemistry for the current pair and accumulate it
            total_chemistry += left_player * right_player

        return total_chemistry  # Return total chemistry sum
