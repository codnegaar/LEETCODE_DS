'''
Graph 1376 Time Needed to Inform All Employees

        A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
        Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee,
        manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
        The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, 
        and they will inform their subordinates, and so on until all employees know about the urgent news.
        The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Please return the minutes needed to inform all the employees about the urgent news.

Example 1:
        Input: n = 1, headID = 0, manager = [-1], informTime = [0]
        Output: 0
        Explanation: The head of the company is the only employee in the company.

Example 2:
        Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
        Output: 1
        Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
        The tree structure of the employees in the company is shown.
         
Constraints:
        1 <= n <= 105
        0 <= headID < n
        manager.length == n
        0 <= manager[i] < n
        manager[headID] == -1
        informTime.length == n
        0 <= informTime[i] <= 1000
        informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.

'''

from typing import List, Tuple, Iterable, Union, Dict

class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
      
        # Define a type alias for Weight, which can be either an integer or a float, representing the time needed to inform subordinates.
        Weight = Union[int, float]
      
        # Define a type alias for a WeightedTree, which is a tuple containing a weight and an iterable of child WeightedTrees.
        WeightedTree = Tuple[Weight, Iterable['WeightedTree']]

        def max_path_sum(tree: WeightedTree) -> Weight:
            """
            Calculate the maximum time required to inform all subordinates recursively.
            """
          
            weight, children = tree
          
            # Sum the current node weight with the maximum of the children's max_path_sum
            return weight + max((max_path_sum(child) for child in children), default=0)

        # Build the tree structure based on the manager relationship
        nodes: Dict[int, Tuple[int, List]] = {i: (inform_time[i], []) for i in range(n)}
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                nodes[mgr][1].append(nodes[employee])

        # Calculate the maximum inform time starting from the head_id
        return max_path_sum(nodes[head_id])

# Example usage
solution = Solution()
n = 6
head_id = 2
manager = [2, 2, -1, 2, 2, 2]
inform_time = [0, 0, 1, 0, 0, 0]
print(solution.numOfMinutes(n, head_id, manager, inform_time))  # Output: 1



# Second Solution
from typing import List, Dict

class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        # Create an adjacency list to represent the employee hierarchy
        subordinates: Dict[int, List[int]] = {i: [] for i in range(n)}
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                subordinates[mgr].append(employee)

        def dfs(employee: int) -> int:
            # If the employee has no subordinates, no additional time is needed
            if not subordinates[employee]:
                return 0
            # Calculate the maximum time needed to inform all subordinates
            return inform_time[employee] + max(dfs(sub) for sub in subordinates[employee])

        # Start DFS from the head manager
        return dfs(head_id)

# Example usage
solution = Solution()
n = 6
head_id = 2
manager = [2, 2, -1, 2, 2, 2]
inform_time = [0, 0, 1, 0, 0, 0]
print(solution.numOfMinutes(n, head_id, manager, inform_time))  # Output: 1
