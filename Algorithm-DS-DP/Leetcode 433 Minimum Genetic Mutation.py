'''
Leetcode 433 Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate 
from startGene to endGene. If there is no such a mutation, return -1.
Note that the starting point is assumed to be valid, so it might not be included in the bank. 

Example 1:
        Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
        Output: 1

Example 2:
        Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        Output: 2

Constraints:
        0 <= bank.length <= 10
        startGene.length == endGene.length == bank[i].length == 8
        startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

'''

from typing import List

class Solution:
    def is_neighbor(self, gene1: str, gene2: str) -> bool:
        """
        Helper function to determine if two gene sequences differ by exactly one mutation.
        
        :param gene1: First gene sequence.
        :param gene2: Second gene sequence.
        :return: True if the sequences differ by exactly one mutation, otherwise False.
        """
        # Count the number of differences between the two gene sequences
        diff_count = sum(1 for a, b in zip(gene1, gene2) if a != b)
        return diff_count == 1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        BFS to find the minimum number of mutations required to reach the end sequence from the start sequence.
        
        :param start: The starting gene sequence.
        :param end: The target gene sequence.
        :param bank: The list of valid gene sequences that can be used in the mutation.
        :return: The minimum number of mutations needed, or -1 if it is not possible.
        """
        if end not in bank:
            return -1

        # Initialize BFS queue and visited set
        queue = [start]
        visited = set([start])
        mutation_count = 0

        while queue:
            next_queue = []
            for current_gene in queue:
                if current_gene == end:
                    return mutation_count
                # Explore all possible mutations in the bank
                for next_gene in bank:
                    if next_gene not in visited and self.is_neighbor(current_gene, next_gene):
                        visited.add(next_gene)
                        next_queue.append(next_gene)
            # Move to the next level of BFS
            queue = next_queue
            mutation_count += 1

        # If we exhaust the queue without finding the end sequence
        return -1

if __name__ == "__main__":
    # Test cases
    assert Solution().minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]) == -1
    assert Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2
