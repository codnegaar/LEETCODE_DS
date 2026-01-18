'''
Leetcode 983 Minimum Cost For Tickets
 
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:
        Input: days = [1,4,6,7,8,20], costs = [2,7,15]
        Output: 11
        Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
        On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
        On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
        In total, you spent $11 and covered all the days of your travel.
        
Example 2:
        Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
        Output: 17
        Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
        On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
        In total, you spent $17 and covered all the days of your travel.
 
Constraints:
        1 <= days.length <= 365
        1 <= days[i] <= 365
        days is in strictly increasing order.
        costs.length == 3
        1 <= costs[i] <= 1000
'''


class Solution:
  def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    ans = 0
    last7 = collections.deque()
    last30 = collections.deque()

    for day in days:
      while last7 and last7[0][0] + 7 <= day:
        last7.popleft()
      while last30 and last30[0][0] + 30 <= day:
        last30.popleft()
      last7.append([day, ans + costs[1]])
      last30.append([day, ans + costs[2]])
      ans = min(ans + costs[0], last7[0][1], last30[0][1])



   # second solution
   from collections import deque
from typing import List

class Solution:
    """
    Class to calculate the minimum cost of travel tickets based on the given travel days and ticket costs.

    Methods:
        mincostTickets(days, costs): Calculates the minimum cost.
    """

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Calculates the minimum cost of travel tickets required for the given travel days and ticket costs.

        Args:
            days (List[int]): A list of integers representing the days of travel.
            costs (List[int]): A list of integers representing the costs of 1-day, 7-day, and 30-day passes.

        Returns:
            int: The minimum cost to cover all the travel days.
        """
        # Initialize queues to store valid cost entries for 7-day and 30-day passes
        last7 = deque()
        last30 = deque()
        total_cost = 0  # Tracks the cumulative minimum cost

        for day in days:
            # Remove expired entries from the 7-day queue
            while last7 and last7[0][0] + 7 <= day:
                last7.popleft()

            # Remove expired entries from the 30-day queue
            while last30 and last30[0][0] + 30 <= day:
                last30.popleft()

            # Add the cost of a 7-day pass for the current day
            last7.append((day, total_cost + costs[1]))
            # Add the cost of a 30-day pass for the current day
            last30.append((day, total_cost + costs[2]))

            # Update the total cost by taking the minimum of:
            # - 1-day pass cost
            # - Cheapest valid 7-day pass
            # - Cheapest valid 30-day pass
            total_cost = min(total_cost + costs[0], last7[0][1], last30[0][1])

        return total_cost

# Unit Tests and Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    days1 = [1, 4, 6, 7, 8, 20]
    costs1 = [2, 7, 15]
    print(f"Minimum cost (Example 1): {solution.mincostTickets(days1, costs1)}")  # Expected: 11

    # Example 2
    days2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs2 = [2, 7, 15]
    print(f"Minimum cost (Example 2): {solution.mincostTickets(days2, costs2)}")  # Expected: 17

    # Unit test function
    def test_mincostTickets():
        assert solution.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
        assert solution.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17
        print("All tests passed!")

    test_mincostTickets()


    return ans


