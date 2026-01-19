'''

Leetcode 2054 Two Best Non-Overlapping Events

You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends
at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such 
that the sum of their values is maximized.
Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time.
More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

Example 1:        
        Input: events = [[1,3,2],[4,5,2],[2,4,3]]
        Output: 4
        Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

Example 2:
        Example 1 Diagram
        Input: events = [[1,3,2],[4,5,2],[1,5,5]]
        Output: 5
        Explanation: Choose event 2 for a sum of 5.

Example 3:
        Input: events = [[1,5,3],[1,5,1],[6,6,5]]
        Output: 8
        Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 
Constraints:
        2 <= events.length <= 105
        events[i].length == 3
        1 <= startTimei <= endTimei <= 109
        1 <= valuei <= 106
'''
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        Finds the maximum sum of values from two non-overlapping events.

        Parameters:
        events (List[List[int]]): A list of events where each event is represented as [start, end, value].

        Returns:
        int: The maximum sum of values from two non-overlapping events.
        """
        n = len(events)

        # Step 1: Sort the events by their start time for binary search compatibility
        events.sort(key=lambda x: x[0])

        # Step 2: Create a suffix array to track the maximum event value from each event onward
        suffixMax = [0] * n
        suffixMax[n - 1] = events[n - 1][2]  # Initialize the last event's value as its own
        
        for i in range(n - 2, -1, -1):
            # Track the maximum value from the current event onward
            suffixMax[i] = max(events[i][2], suffixMax[i + 1])

        # Step 3: Iterate through each event to calculate the maximum sum of two events
        maxSum = 0
        
        for i in range(n):
            left, right = i + 1, n - 1
            nextEventIndex = -1

            # Perform binary search to find the next event that starts after the current event ends
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:  # Ensure no overlap
                    nextEventIndex = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Calculate the maximum sum including the current event
            if nextEventIndex != -1:
                maxSum = max(maxSum, events[i][2] + suffixMax[nextEventIndex])
            
            # Also consider the case where we only take the current event
            maxSum = max(maxSum, events[i][2])

        return maxSum

# Unit Tests
def test_maxTwoEvents():
    solution = Solution()
    
    # Test Case 1: Non-overlapping events
    events1 = [[1, 3, 4], [4, 5, 6], [6, 7, 2]]
    assert solution.maxTwoEvents(events1) == 10, "Test Case 1 Failed"

    # Test Case 2: Overlapping events
    events2 = [[1, 3, 4], [2, 5, 6], [6, 7, 2]]
    assert solution.maxTwoEvents(events2) == 8, "Test Case 2 Failed"

    # Test Case 3: Single event
    events3 = [[1, 3, 4]]
    assert solution.maxTwoEvents(events3) == 4, "Test Case 3 Failed"

    # Test Case 4: Mixed overlapping and non-overlapping
    events4 = [[1, 3, 4], [3, 4, 5], [5, 6, 6]]
    assert solution.maxTwoEvents(events4) == 11, "Test Case 4 Failed"

    # Test Case 5: Events with zero value
    events5 = [[1, 2, 0], [3, 4, 0], [5, 6, 10]]
    assert solution.maxTwoEvents(events5) == 10, "Test Case 5 Failed"

    print("All test cases passed!")

# Run Tests
test_maxTwoEvents()



