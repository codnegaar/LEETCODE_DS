'''

433 Minimum Genetic Mutation
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such mutation, return -1.

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

class Solution:
    def is_neighbor(self, p, q):
        diff = 0
        for a, b in zip(p, q):
            if a != b:
                diff += 1
            if diff > 1:
                return False
        return True

    def minMutation(self, start, end, bank):
        """
        BFS, record level and avoid loop

        Similar to 127 Word Ladder

        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        q = [start]
        visited = {start}
        lvl = 0
        while q:
            cur_q = []
            for e in q:
                if e == end:
                    return lvl
                for t in bank:
                    if t not in visited and self.is_neighbor(e, t):
                        visited.add(t)
                        cur_q.append(t)

            lvl += 1
            q = cur_q

        return -1


if __name__ == "__main__":
    assert Solution().minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]) == -1
    assert Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2

