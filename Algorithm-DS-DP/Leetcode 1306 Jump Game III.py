'''
Leetcode 1306 Jump Game III

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
Notice that you can not jump outside of the array at any time.

Example 1:
        Input: arr = [4,2,3,0,3,1,2], start = 5
        Output: true
        Explanation: 
        All possible ways to reach at index 3 with value 0 are: 
        index 5 -> index 4 -> index 1 -> index 3 
        index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:
        Input: arr = [4,2,3,0,3,1,2], start = 0
        Output: true 
        Explanation: 
        One possible way to reach at index 3 with value 0 is: 
        index 0 -> index 4 -> index 1 -> index 3
Example 3:
        Input: arr = [3,0,2,1,2], start = 2
        Output: false
        Explanation: There is no way to reach at index 1 with value 0.
         

Constraints:
        1 <= arr.length <= 5 * 104
        0 <= arr[i] < arr.length
        0 <= start < arr.length
'''

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        Function to determine if it's possible to reach an index with value 0 starting from a given index.
        
        Parameters:
        arr (List[int]): The array of non-negative integers, where each value represents the maximum jump length.
        start (int): The starting index in the array.
        
        Returns:
        bool: True if it is possible to reach an index with value 0, otherwise False.
        """
        # Array to keep track of visited indices.
        visited = [False] * len(arr)
        # Initialize queue for Breadth-First Search (BFS) with the starting position.
        queue = [start]
        
        while queue:
            current = queue.pop(0)
            # If we reach an index with value 0, return True.
            if arr[current] == 0:
                return True
            
            # Mark the current index as visited.
            visited[current] = True
            
            # Calculate possible next moves: left and right.
            for next_index in (current - arr[current], current + arr[current]):
                # If the next index is within bounds and has not been visited, add it to the queue.
                if 0 <= next_index < len(arr) and not visited[next_index]:
                    queue.append(next_index)
        
        # If we exhaust all possibilities without finding a 0, return False.
        return False
