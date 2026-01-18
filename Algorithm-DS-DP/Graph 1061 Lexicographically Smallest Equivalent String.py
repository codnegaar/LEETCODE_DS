'''
Graph 1061 Lexicographically Smallest Equivalent String

You are given two strings of the same length s1 and s2 and a string baseStr.
We say s1[i] and s2[i] are equivalent characters.
For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:
        
        Reflexivity: 'a' == 'a'.
        Symmetry: 'a' == 'b' implies 'b' == 'a'.
        Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
        For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.
        Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2. 

Example 1:
        Input: s1 = "parker", s2 = "morris", baseStr = "parser"
        Output: "makkek"
        Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
        The characters in each group are equivalent and sorted in lexicographical order.
        So the answer is "makkek".

Example 2:
        Input: s1 = "hello", s2 = "world", baseStr = "hold"
        Output: "hdld"
        Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
        So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".

Example 3:
        Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
        Output: "aauaaaaada"
        Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
      
Constraints:
        1 <= s1.length, s2.length, baseStr <= 1000
        s1.length == s2.length
        s1, s2, and baseStr consist of lowercase English letters.
'''

class DisjointSets:
    """
    Disjoint Sets for union-find operations with path compression.
    
    Attributes:
    - parent: Dictionary to hold the parent of each element.
    """

    def __init__(self):
        self.parent = {}

    def find(self, u):
        """
        Finds the root of element `u` with path compression.
        
        Parameters:
        - u: The element to find the root of.
        
        Returns:
        - The root representative of the element.
        """
        if u not in self.parent:
            self.parent[u] = u
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        """
        Unites the sets containing `u` and `v` by lexicographically smaller root.
        
        Parameters:
        - u, v: Elements to unite.
        """
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Attach the root of the lexicographically larger element to the smaller
            if root_u < root_v:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Constructs the lexicographically smallest equivalent string for `baseStr`
        using character equivalences defined by pairs in `s1` and `s2`.
        
        Parameters:
        - s1, s2: Two strings of equal length, where each character pair (s1[i], s2[i])
          denotes equivalent characters.
        - baseStr: The input string to transform using the defined equivalences.
        
        Returns:
        - A string where each character in `baseStr` is replaced by the smallest
          lexicographical equivalent character.
        """
        ds = DisjointSets()

        # Build equivalence groups for characters in s1 and s2
        for char1, char2 in zip(s1, s2):
            ds.union(char1, char2)

        # Transform baseStr by finding the lexicographically smallest equivalent
        transformed_str = [ds.find(char) for char in baseStr]
        return ''.join(transformed_str)
