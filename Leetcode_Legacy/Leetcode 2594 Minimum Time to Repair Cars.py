'''
Leetcode 2594 Minimum Time to Repair Cars

You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.
You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.
Return the minimum time taken to repair all the cars.
Note: All the mechanics can repair the cars simultaneously.

Example 1:
        Input: ranks = [4,2,3,1], cars = 10
        Output: 16
        Explanation: 
        - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
        - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
        - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
        - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
        It can be proved that the cars cannot be repaired in less than 16 minutes.ΓÇïΓÇïΓÇïΓÇïΓÇï

Example 2:
        Input: ranks = [5,1,8], cars = 6
        Output: 16
        Explanation: 
        - The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
        - The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
        - The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
        It can be proved that the cars cannot be repaired in less than 16 minutes.ΓÇïΓÇïΓÇïΓÇïΓÇï         

Constraints:
        1 <= ranks.length <= 105
        1 <= ranks[i] <= 100
        1 <= cars <= 106

'''

from typing import List
from math import isqrt

class Solution:
    """
    A class to determine the minimum time required to repair a given number of cars 
    using mechanics with different efficiency levels (ranks).
    """

    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        Finds the minimum time required to repair all `cars`, given a list of 
        mechanic ranks, where the time taken by a mechanic with rank `r` to repair 
        `x` cars is `(x^2 * r)`.

        Parameters:
        ranks (List[int]): A list of mechanic ranks.
        cars (int): The number of cars to be repaired.

        Returns:
        int: The minimum time required to repair all cars.
        """

        # Binary search range: [1, max possible time] based on mechanics count
        num_mechanics = len(ranks)
        left, right = 1, (((cars // num_mechanics) + 1) ** 2) * max(ranks)

        def canRepairInTime(time_limit: int) -> bool:
            """
            Checks if all cars can be repaired within `time_limit` using available mechanics.

            Parameters:
            time_limit (int): The maximum time allowed to repair all cars.

            Returns:
            bool: True if `cars` can be repaired in `time_limit`, otherwise False.
            """
            total_cars_repaired = sum(isqrt(time_limit // r) for r in ranks)
            return total_cars_repaired >= cars

        # Binary search to find the minimum repair time
        while left < right:
            mid = (left + right) // 2  # Midpoint as the current time guess
            if canRepairInTime(mid):
                right = mid  # Try a smaller time limit
            else:
                left = mid + 1  # Increase time limit

        return left  # The minimum valid repair time
