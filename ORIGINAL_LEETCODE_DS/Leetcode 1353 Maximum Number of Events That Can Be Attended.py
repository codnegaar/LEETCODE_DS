'''
Leetcode 1353 Maximum Number of Events That Can Be Attended
 
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
Return the maximum number of events you can attend. 

Example 1:
        Input: events = [[1,2],[2,3],[3,4]]
        Output: 3
        Explanation: You can attend all the three events.
        One way to attend them all is as shown.
        Attend the first event on day 1.
        Attend the second event on day 2.
        Attend the third event on day 3.

Example 2:
        Input: events= [[1,2],[2,3],[3,4],[1,2]]
        Output: 4 

Constraints:
        1 <= events.length <= 105
        events[i].length == 2
        1 <= startDayi <= endDayi <= 105

'''
from heapq import heappush, heappop
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Finds the maximum number of events that can be attended.
        
        Each event is represented as [start_day, end_day]. You can attend at most one event per day.
        
        Parameters:
        events (List[List[int]]): A list of events, each with a start and end day.
        
        Returns:
        int: The maximum number of events that can be attended.
        """
        # Sort events by start day
        events.sort()

        total_events = len(events)
        event_index = 0
        attended = 0
        min_heap = []

        # Find the last possible day we may need to attend an event
        last_day = max(end for _, end in events)

        # Iterate over each day from 1 to the last event's end day
        for day in range(1, last_day + 1):
            # Add events that start today to the heap
            while event_index < total_events and events[event_index][0] == day:
                heappush(min_heap, events[event_index][1])
                event_index += 1

            # Remove events from the heap that have already expired
            while min_heap and min_heap[0] < day:
                heappop(min_heap)

            # Attend the event that ends the earliest (greedy choice)
            if min_heap:
                heappop(min_heap)
                attended += 1

        return attended
