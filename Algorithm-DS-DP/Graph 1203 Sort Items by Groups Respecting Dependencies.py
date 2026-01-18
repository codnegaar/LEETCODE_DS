'''
Graph 1203 Sort Items by Groups Respecting Dependencies

There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group.
The items and the groups are zero-indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:
        The items that belong to the same group are next to each other in the sorted list.
        There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
        Return any solution if there is more than one solution and return an empty list if there is no solution.

Example 1:
        Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
        Output: [6,3,4,1,5,2,0,7]

Example 2:
        Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
        Output: []
        Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
         
Constraints:
        1 <= m <= n <= 3 * 104
        group.length == beforeItems.length == n
        -1 <= group[i] <= m - 1
        0 <= beforeItems[i].length <= n - 1
        0 <= beforeItems[i][j] <= n - 1
        i != beforeItems[i][j]
        beforeItems[i] does not contain duplicate elements.
'''
from typing import List, Dict
from collections import defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        Sorts items given their group affiliations and dependency constraints.
        
        Parameters:
        n (int): Total number of items.
        m (int): Total number of groups.
        group (List[int]): List of group affiliations for each item, where -1 indicates no group.
        beforeItems (List[List[int]]): List of dependencies for each item.
        
        Returns:
        List[int]: Ordered list of items if possible, otherwise an empty list if sorting is not feasible.
        """
        
        # Step 1: Initialize data structures
        # Map items to their groups; ungrouped items are given unique virtual group identifiers
        group_map = defaultdict(list)
        for i in range(n):
            group_id = str(i) + '*' if group[i] == -1 else group[i]
            group_map[group_id].append(i)

        # Build graphs for group and item dependencies
        group_graph = defaultdict(set)  # Group dependencies
        item_graph = defaultdict(list)  # Item dependencies
        
        # Step 2: Populate dependency graphs
        for i in range(n):
            for b in beforeItems[i]:
                item_graph[i].append(b)
                if group[i] != group[b]:  # If items belong to different groups
                    src = str(i) + '*' if group[i] == -1 else group[i]
                    dest = str(b) + '*' if group[b] == -1 else group[b]
                    group_graph[src].add(dest)
        
        # Helper function for topological sort using DFS
        def dfs(node, result, visited, graph):
            if node in visited:  # Cycle detected
                return visited[node]
            visited[node] = True
            for neighbor in graph[node]:
                if dfs(neighbor, result, visited, graph):
                    return True
            visited[node] = False  # Mark node as fully processed
            result.append(node)
            return False

        # Step 3: Topologically sort the groups
        group_order = []
        visited_groups = {}
        for group_id in group_map:
            if dfs(group_id, group_order, visited_groups, group_graph):
                return []  # Cycle detected in group dependencies

        # Step 4: Topologically sort items within each group and accumulate final result
        result = []
        visited_items = {}
        for g in group_order:
            for item in group_map[g]:
                if dfs(item, result, visited_items, item_graph):
                    return []  # Cycle detected in item dependencies
        
        return result



# Second solution

from typing import List, Dict
from collections import defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        Sorts items given their group affiliations and dependency constraints.
        
        Parameters:
        n (int): Total number of items.
        m (int): Total number of groups.
        group (List[int]): List of group affiliations for each item, where -1 indicates no group.
        beforeItems (List[List[int]]): List of dependencies for each item.
        
        Returns:
        List[int]: Ordered list of items if possible, otherwise an empty list if sorting is not feasible.
        """
        
        # Step 1: Initialize data structures
        # Map items to their groups; ungrouped items are given unique virtual group identifiers
        group_map = defaultdict(list)
        for i in range(n):
            group_id = str(i) + '*' if group[i] == -1 else group[i]
            group_map[group_id].append(i)

        # Build graphs for group and item dependencies
        group_graph = defaultdict(set)  # Group dependencies
        item_graph = defaultdict(list)  # Item dependencies
        
        # Step 2: Populate dependency graphs
        for i in range(n):
            for b in beforeItems[i]:
                item_graph[i].append(b)
                if group[i] != group[b]:  # If items belong to different groups
                    src = str(i) + '*' if group[i] == -1 else group[i]
                    dest = str(b) + '*' if group[b] == -1 else group[b]
                    group_graph[src].add(dest)
        
        # Helper function for topological sort using DFS
        def dfs(node, result, visited, graph):
            if node in visited:  # Cycle detected
                return visited[node]
            visited[node] = True
            for neighbor in graph[node]:
                if dfs(neighbor, result, visited, graph):
                    return True
            visited[node] = False  # Mark node as fully processed
            result.append(node)
            return False

        # Step 3: Topologically sort the groups
        group_order = []
        visited_groups = {}
        for group_id in group_map:
            if dfs(group_id, group_order, visited_groups, group_graph):
                return []  # Cycle detected in group dependencies

        # Step 4: Topologically sort items within each group and accumulate final result
        result = []
        visited_items = {}
        for g in group_order:
            for item in group_map[g]:
                if dfs(item, result, visited_items, item_graph):
                    return []  # Cycle detected in item dependencies
        
        return result







