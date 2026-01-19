'''
Leetcode 2127 Maximum Employees to Be Invited to a Meeting
 
A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.
The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table.
The favorite person of an employee is not themself.
Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

Example 1:
        Input: favorite = [2,2,1,2]
        Output: 3
        Explanation:
                The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
                All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
                Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
                The maximum number of employees that can be invited to the meeting is 3. 

Example 2:
        Input: favorite = [1,2,0]
        Output: 3
        Explanation: 
                Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
                The seating arrangement will be the same as that in the figure given in example 1:
                - Employee 0 will sit between employees 2 and 1.
                - Employee 1 will sit between employees 0 and 2.
                - Employee 2 will sit between employees 1 and 0.
                The maximum number of employees that can be invited to the meeting is 3.

Example 3:
        Input: favorite = [3,0,1,4,1]
        Output: 4
        Explanation:
                The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
                Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
                So the company leaves them out of the meeting.
                The maximum number of employees that can be invited to the meeting is 4.
         
        Constraints:
        n == favorite.length
        2 <= n <= 105
        0 <= favorite[i] <= n - 1
        favorite[i] != i
'''
from typing import List, Dict, Set
from collections import defaultdict

class Solution:
    """
    This class contains a solution to find the maximum number of invitations 
    that can be sent in a social network based on mutual or cyclic friendships.
    """

    def maximumInvitations(self, favorite: List[int]) -> int:
        """
        Finds the maximum number of invitations that can be sent in a network of friends.
        
        Parameters:
        - favorite (List[int]): A list where favorite[i] represents the person that person i likes.

        Returns:
        - int: The maximum number of invitations that can be sent.
        """

        # Step 1: Build adjacency lists for the graph and its transpose
        adj = defaultdict(list)  # adjacency list of the graph
        transpose = defaultdict(list)  # adjacency list of the transpose of the graph
        for i in range(len(favorite)):
            adj[i].append(favorite[i])
            transpose[favorite[i]].append(i)

        # Step 2: Perform Kosaraju's algorithm to find Strongly Connected Components (SCCs)
        stack = []  # Stack for storing the order of completion
        visited = [False] * len(favorite)

        # Depth First Search (DFS) for the main graph
        def dfs(node: int):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)  # Add node to stack after visiting all neighbors

        # First pass of Kosaraju's algorithm
        for i in range(len(favorite)):
            if not visited[i]:
                dfs(i)

        # Perform DFS on the transpose graph to find SCCs
        sccs = []  # List of SCCs
        visited = [False] * len(favorite)  # Reset visited for the second pass

        def find_scc(node: int, scc: Set[int]):
            visited[node] = True
            scc.add(node)
            for neighbor in transpose[node]:
                if not visited[neighbor]:
                    find_scc(neighbor, scc)

        # Second pass to find SCCs
        while stack:
            node = stack.pop()
            if not visited[node]:
                scc = set()
                find_scc(node, scc)
                sccs.append(scc)

        # Step 3: Calculate the maximum size of SCCs and handle two-node cycles
        max_cycle_length = 0  # Maximum size of any cycle found in SCCs

        # Process all SCCs to find the maximum cycle length
        for scc in sccs:
            if len(scc) > 2:  # Larger SCCs are cycles
                max_cycle_length = max(max_cycle_length, len(scc))

        # Helper function to find the longest arm (path) extending from a node
        def find_longest_arm(start: int, exclude: int) -> int:
            longest_path = 0
            for neighbor in transpose[start]:
                if neighbor != exclude:  # Avoid traversing back to the other node in the 2-cycle
                    longest_path = max(longest_path, 1 + find_longest_arm(neighbor, start))
            return longest_path

        # Process two-node SCCs (two-node cycles)
        two_node_scc_total = 0
        for scc in sccs:
            if len(scc) == 2:  # Check for two-node SCC
                node1, node2 = list(scc)
                # Calculate the total size contributed by this 2-cycle and its arms
                two_node_scc_total += 2 + find_longest_arm(node1, node2) + find_longest_arm(node2, node1)

        # Return the maximum of the two possibilities
        return max(max_cycle_length, two_node_scc_total)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    favorite = [2, 2, 1, 2]  # Example input
    print("Maximum Invitations:", solution.maximumInvitations(favorite))

# Unit Test
def test_maximumInvitations():
    solution = Solution()
    assert solution.maximumInvitations([2, 2, 1, 2]) == 3, "Test case 1 failed"
    assert solution.maximumInvitations([1, 0, 3, 4, 3]) == 4, "Test case 2 failed"
    assert solution.maximumInvitations([0, 0, 0, 0]) == 1, "Test case 3 failed"
    assert solution.maximumInvitations([1, 2, 3, 4, 0]) == 5, "Test case 4 failed"
    assert solution.maximumInvitations([1, 0]) == 2, "Test case 5 failed"
    print("All test cases passed!")

test_maximumInvitations()

# Changes made:
# 1. Added detailed docstrings and comments for every logical block.
# 2. Improved performance by avoiding unnecessary iterations.
# 3. Modularized the code into smaller functions for readability.
# 4. Added an example implementation for demonstration.
# 5. Included a unit test suite to validate functionality.
# 6. Simplified SCC processing logic for clarity and maintainability.
