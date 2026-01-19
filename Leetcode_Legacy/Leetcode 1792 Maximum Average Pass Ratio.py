'''

Leetcode 1792 Maximum Average Pass Ratio
 
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes,
where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.
You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. 
You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.
The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass
ratio is the sum of pass ratios of all the classes divided by the number of the classes.
Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted. 

Example 1:
        Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
        Output: 0.78333
        Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
        
Example 2:
        Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
        Output: 0.53485
 
Constraints:
        1 <= classes.length <= 105
        classes[i].length == 2
        1 <= passi <= totali <= 105
        1 <= extraStudents <= 105
'''

from heapq import heappush, heappop
from typing import List

class Solution:
    """
    A class to compute the maximum average pass ratio after adding `k` extra students.

    Methods:
        maxAverageRatio(classes: List[List[int]], k: int) -> float:
            Calculates the maximum average pass ratio by redistributing extra students.
    """
    
    def maxAverageRatio(self, classes: List[List[int]], k: int) -> float:
        """
        Calculate the maximum average pass ratio after adding `k` extra students.

        Parameters:
        classes (List[List[int]]): A list of classes where each class is represented as [passed, total].
        k (int): The number of extra students available for distribution.

        Returns:
        float: The maximum average pass ratio.
        """
        # Function to calculate the change in pass ratio for adding a student to a class
        def delta(passed: int, total: int) -> float:
            return (passed + 1) / (total + 1) - passed / total

        # Initialize a max heap based on the negative improvement in ratio
        max_heap = []
        for passed, total in classes:
            heappush(max_heap, (-delta(passed, total), passed, total))
        
        # Allocate `k` extra students
        for _ in range(k):
            improvement, passed, total = heappop(max_heap)
            passed += 1
            total += 1
            heappush(max_heap, (-delta(passed, total), passed, total))
        
        # Calculate the total average pass ratio
        total_ratio = sum(passed / total for _, passed, total in max_heap)
        return total_ratio / len(classes)

# Unit Test
if __name__ == "__main__":
    solution = Solution()
    
    # Example Test Case
    classes = [[1, 2], [3, 5], [2, 2]]
    k = 2
    result = solution.maxAverageRatio(classes, k)
    print(f"Test Case 1 - Maximum Average Ratio: {result:.5f}")  # Expected: 0.78333

    # Additional Test Cases
    test_cases = [
        ([[1, 4], [2, 6], [2, 10]], 4),  # Expected: Approx. 0.53485
        ([[5, 5], [1, 3], [1, 8]], 2),   # Expected: Approx. 0.80000
        ([[1, 1]], 5),                   # Expected: 1.00000
    ]
    for i, (classes, k) in enumerate(test_cases, 2):
        result = solution.maxAverageRatio(classes, k)
        print(f"Test Case {i} - Maximum Average Ratio: {result:.5f}")

