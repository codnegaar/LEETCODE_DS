'''
Leetcode 2551 Put Marbles in Bags

You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.
Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.
Return the difference between the maximum and minimum scores among marble distributions.

Example 1:
        Input: weights = [1,3,5,1], k = 2
        Output: 4
        Explanation: 
        The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
        The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
        Thus, we return their difference 10 - 6 = 4.

Example 2:
        Input: weights = [1, 3], k = 2
        Output: 0
        Explanation: The only distribution possible is [1],[3]. 
        Since both the maximal and minimal score are the same, we return 0.
 

Constraints:        
        1 <= k <= weights.length <= 105
        1 <= weights[i] <= 109


'''
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        Calculates the difference between the maximum and minimum possible scores
        after splitting the weights into k groups using the described scoring rule.

        Parameters:
        weights (List[int]): List of marble weights.
        k (int): Number of groups to split the marbles into.

        Returns:
        int: The difference between the max and min possible scores.
        """
        # If only one group, score is fixed ΓÇö no difference to compute
        if k == 1:
            return 0

        # Generate all adjacent pair sums, since splits happen between two weights
        pair_sums = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]

        # Sort the pair sums to easily pick the smallest and largest (k-1) splits
        pair_sums.sort()

        # Minimum score: sum of smallest (k-1) splits
        min_score = sum(pair_sums[:k - 1])

        # Maximum score: sum of largest (k-1) splits
        max_score = sum(pair_sums[-(k - 1):])

        # Return the score difference
        return max_score - min_score
