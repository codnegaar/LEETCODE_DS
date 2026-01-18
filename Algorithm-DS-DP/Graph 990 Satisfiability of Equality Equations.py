'''

Graph 990 Satisfiability of Equality Equations

You are given an array of string equations that represent relationships between variables where each string equation [i] is of length 4 and 
takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

        Example 1:
        Input: equations = ["a==b","b!=a"]
        Output: false
        Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
        There is no way to assign the variables to satisfy both equations.

Example 2:
        Input: equations = ["b==a","a==b"]
        Output: true
        Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
         

Constraints:
        1 <= equations.length <= 500
        equations[i].length == 4
        equations[i][0] is a lowercase letter.
        equations[i][1] is either '=' or '!'.
        equations[i][2] is '='.
        equations[i][3] is a lowercase letter.

'''

from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        Determines if it is possible to satisfy all given equations.

        Uses union-find (disjoint-set) to group variables with equal relationships
        and ensures that no conflicting relationships exist in the final structure.

        Parameters:
        equations (List[str]): A list of equations as strings, where each equation is 
                               in the form 'a==b' or 'a!=b'.

        Returns:
        bool: True if it is possible to satisfy all equations, False otherwise.
        """

        # Initialize an array where each variable is its own root at the start.
        root = list(range(26))  # for variables 'a' to 'z'

        # Helper function to find the root of a variable x with path compression.
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])  # Path compression to make future finds faster
            return root[x]

        # Helper function to union the components of variables x and y.
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                root[root_x] = root_y  # Union the roots, choosing root_y as the root

        # First pass: Union variables that must be equal.
        for equation in equations:
            if equation[1] == '=':  # Equal relationship
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                union(x, y)

        # Second pass: Check that variables in inequality relations are not connected.
        for equation in equations:
            if equation[1] == '!':  # Not equal relationship
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                if find(x) == find(y):  # Conflict if x and y have the same root
                    return False

        return True
