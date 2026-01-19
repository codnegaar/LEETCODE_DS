'''

Graph 997 Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
        There is exactly one person that satisfies properties 1 and 2.
        You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. 
        If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
        Input: n = 2, trust = [[1,2]]
        Output: 2

Example 2:
        Input: n = 3, trust = [[1,3],[2,3]]
        Output: 3

Example 3:
        Input: n = 3, trust = [[1,3],[2,3],[3,1]]
        Output: -1 

Constraints:
        1 <= n <= 1000
        0 <= trust.length <= 104
        trust[i].length == 2
        All the pairs of trust are unique.
        ai != bi
        1 <= ai, bi <= n

'''


from collections import Counter

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1 if not trust else -1
        
        # Count how many people each person trusts and how many trust each person
        trusts = Counter(t for t, _ in trust)
        trusted_by = Counter(t for _, t in trust)

        # Find the judge candidate
        for person in range(1, n + 1):
            if trusts[person] == 0 and trusted_by[person] == n - 1:
                return person

        return -1



# Second solution

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Determines the "judge" in a town based on trust relationships.

        Parameters:
        n (int): The number of people in the town.
        trust (List[List[int]]): A list of pairs [a, b] indicating that person a trusts person b.

        Returns:
        int: The label of the town judge if one exists, otherwise -1.
        """
        # Edge case: If there's only one person and no trust relationships, they are the judge.
        if n == 1:
            return 1 if not trust else -1
        
        # Initialize trust counts with 0 for each person.
        trust_count = [0] * (n + 1)
        
        # For each trust pair, decrease the count for the truster and increase for the trusted.
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        
        # The judge should be trusted by everyone else (n-1) and trust no one.
        for person in range(1, n + 1):
            if trust_count[person] == n - 1:
                return person
        
        # If no judge is found, return -1.
        return -1


