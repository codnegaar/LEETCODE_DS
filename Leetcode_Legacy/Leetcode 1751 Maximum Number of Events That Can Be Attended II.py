'''

Leetcode 1751 Maximum Number of Events That Can Be Attended II

You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, 
you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot
attend two events where one of them starts and the other ends on the same day.
Return the maximum sum of values that you can receive by attending events. 

Example 1:
        Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
        Output: 7
        Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.

Example 2:
        Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
        Output: 10
        Explanation: Choose event 2 for a total value of 10.
        Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
        
Example 3:
        Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
        Output: 9
        Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
         
Constraints:
        1 <= k <= events.length
        1 <= k * events.length <= 106
        1 <= startDayi <= endDayi <= 109
        1 <= valuei <= 106

'''

from functools import lru_cache
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        Finds the maximum total value by attending at most `k` non-overlapping events.

        Parameters:
        - events (List[List[int]]): A list where each event is represented as [start, end, value].
        - k (int): The maximum number of events that can be attended.

        Returns:
        - int: The maximum value achievable by attending up to `k` non-overlapping events.
        """

        # Sort events by their start time
        events.sort()

        # Precompute next possible non-overlapping event indices using binary search
        start_times = [event[0] for event in events]

        def find_next_index(current_end):
            """
            Finds the index of the next event that starts after the current event's end.
            """
            left, right = 0, len(events)
            while left < right:
                mid = (left + right) // 2
                if start_times[mid] > current_end:
                    right = mid
                else:
                    left = mid + 1
            return left

        @lru_cache(maxsize=None)
        def dp(index: int, remaining: int) -> int:
            """
            Recursive function with memoization to get the max value by either
            skipping or taking the current event.

            Parameters:
            - index (int): Current event index.
            - remaining (int): Remaining events we can attend.

            Returns:
            - int: Maximum value achievable from this state.
            """
            if index == len(events) or remaining == 0:
                return 0

            # Option 1: Skip current event
            skip = dp(index + 1, remaining)

            # Option 2: Attend current event, then jump to next non-overlapping event
            next_index = find_next_index(events[index][1])
            take = events[index][2] + dp(next_index, remaining - 1)

            return max(skip, take)

        return dp(0, k)
