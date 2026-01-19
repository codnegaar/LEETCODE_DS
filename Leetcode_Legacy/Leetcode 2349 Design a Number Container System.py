'''
Leetcode 2349 Design a Number Container System

Design a number container system that can do the following:
        Insert or Replace a number at the given index in the system.
        Return the smallest index for the given number in the system.
Implement the NumberContainers class:
        NumberContainers() Initializes the number container system.
        void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
        int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
      
Example 1:
        Input
                ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
                [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
        Output
                [null, -1, null, null, null, null, 1, null, 2]
        
        Explanation
                NumberContainers nc = new NumberContainers();
                nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
                nc.change(2, 10); // Your container at index 2 will be filled with number 10.
                nc.change(1, 10); // Your container at index 1 will be filled with number 10.
                nc.change(3, 10); // Your container at index 3 will be filled with number 10.
                nc.change(5, 10); // Your container at index 5 will be filled with number 10.
                nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
                nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
                nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
                 
Constraints:
1 <= index, number <= 109
At most 105 calls will be made in total to change and find.

'''

"""
LeetCode 2349: Design a Number Container System
URL: https://leetcode.com/problems/design-a-number-container-system/description/

This class implements a Number Container System using a dictionary and a min-heap
for efficient retrieval of the smallest index for a given number.

Reference:
Python Heapq Documentation: https://docs.python.org/3/library/heapq.html
"""

import heapq

class NumberContainers:
    """
    NumberContainers stores indices with associated numbers and provides an efficient way 
    to retrieve the smallest index containing a specific number.

    Attributes:
    -----------
    index_to_value : dict
        Maps indices to their assigned numbers.
    value_to_heap : dict
        Maps numbers to a min-heap (list) containing indices where the number is stored.
    """

    def __init__(self):
        """Initialize dictionaries to store index-number mappings and min-heaps for quick retrieval."""
        self.index_to_value = {}  # Maps index -> number
        self.value_to_heap = {}   # Maps number -> min-heap of indices

    def change(self, index: int, number: int) -> None:
        """
        Assigns a number to an index. If the number is new, it initializes a heap for it.

        Parameters:
        -----------
        index : int
            The index to be updated.
        number : int
            The number to assign to the index.

        Time Complexity:
        ---------------
        O(log N) (heap push operation)
        """
        self.index_to_value[index] = number  # Update mapping of index to number
        
        # If the number is not present, initialize a heap
        if number not in self.value_to_heap:
            self.value_to_heap[number] = []
        
        # Push the index into the min-heap of the number
        heapq.heappush(self.value_to_heap[number], index)

    def find(self, number: int) -> int:
        """
        Finds the smallest index where the given number is stored.

        Parameters:
        -----------
        number : int
            The number to search for.

        Returns:
        --------
        int
            The smallest index containing the number, or -1 if not found.

        Time Complexity:
        ---------------
        Amortized O(1) - While loop ensures stale indices are removed efficiently.
        """
        if number not in self.value_to_heap:
            return -1  # If number doesn't exist, return -1

        heap = self.value_to_heap[number]  # Reference to the min-heap
        
        # Clean up stale indices (indices that do not match the number anymore)
        while heap:
            smallest_index = heap[0]  # Peek at the smallest index
            if self.index_to_value.get(smallest_index) == number:
                return smallest_index  # Return valid index
            heapq.heappop(heap)  # Remove outdated index
        
        return -1  # No valid index found

# Example Implementation:
if __name__ == "__main__":
    obj = NumberContainers()
    obj.change(1, 10)  # Assign number 10 to index 1
    obj.change(2, 20)  # Assign number 20 to index 2
    obj.change(3, 10)  # Assign number 10 to index 3
    obj.change(2, 10)  # Change index 2 to number 10

    print(obj.find(10))  # Expected Output: 1 (smallest index containing 10)
    print(obj.find(20))  # Expected Output: -1 (since index 2 was changed from 20 to 10)

 
 

