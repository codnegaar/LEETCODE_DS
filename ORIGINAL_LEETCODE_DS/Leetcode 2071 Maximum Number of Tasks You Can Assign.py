'''
Leetcode 2071 Maximum Number of Tasks You Can Assign
 
You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete.
The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single
task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).
Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may
only give each worker at most one magical pill.
Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

Example 1:
        Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
        Output: 3
        Explanation:
        We can assign the magical pill and tasks as follows:
        - Give the magical pill to worker 0.
        - Assign worker 0 to task 2 (0 + 1 >= 1)
        - Assign worker 1 to task 1 (3 >= 2)
        - Assign worker 2 to task 0 (3 >= 3)
        
Example 2:
        Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
        Output: 1
        Explanation:
        We can assign the magical pill and tasks as follows:
        - Give the magical pill to worker 0.
        - Assign worker 0 to task 0 (0 + 5 >= 5)

Example 3:
        Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
        Output: 2
        Explanation:
        We can assign the magical pills and tasks as follows:
        - Give the magical pill to worker 0 and worker 1.
        - Assign worker 0 to task 0 (0 + 10 >= 10)
        - Assign worker 1 to task 1 (10 + 10 >= 15)
        The last pill is not given because it will not make any worker strong enough for the last task.
 
Constraints:        
        n == tasks.length
        m == workers.length
        1 <= n, m <= 5 * 104
        0 <= pills <= m
        0 <= tasks[i], workers[j], strength <= 109

'''
from typing import List
from bisect import bisect_left
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        Determines the maximum number of tasks that can be assigned to workers
        given task difficulty, worker strength, number of pills (each adds `strength`), 
        and the condition that each pill can be used once per worker.

        Parameters:
        - tasks (List[int]): List of task difficulty levels.
        - workers (List[int]): List of worker strength levels.
        - pills (int): Number of strength-boosting pills available.
        - strength (int): Additional strength each pill provides.

        Returns:
        - int: Maximum number of tasks that can be assigned.
        """

        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        def can_assign(k: int) -> bool:
            """
            Checks if k tasks can be assigned given the current pill and strength constraints.
            """
            p = pills
            available_workers = SortedList(workers[m - k:])  # k strongest workers

            for i in range(k - 1, -1, -1):  # Iterate from hardest task to easiest
                task = tasks[i]

                if available_workers[-1] >= task:
                    # Assign the strongest available worker
                    available_workers.pop()
                else:
                    if p == 0:
                        return False  # No pills left to boost any worker
                    # Find the weakest worker who, when boosted, can do the task
                    idx = available_workers.bisect_left(task - strength)
                    if idx == len(available_workers):
                        return False  # No worker can do the task even with a pill
                    available_workers.pop(idx)
                    p -= 1  # Use one pill
            return True

        # Binary search to find the maximum number of tasks assignable
        low, high, result = 0, min(n, m), 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result
