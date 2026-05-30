'''

Leetcode 3161 Block Placement Queries

There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.
        You are given a 2D array queries, which contains two types of queries:
        For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
        For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies 
        in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
        Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.
        
         

Example 1:
        Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
        Output: [false,true,true]
        Explanation:
        For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

Example 2:
        Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
        Output: [true,true,false]
        Explanation:
        Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
        Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.
         

Constraints:
        1 <= queries.length <= 15 * 104
        2 <= queries[i].length <= 3
        1 <= queries[i][0] <= 2
        1 <= x, sz <= min(5 * 104, 3 * queries.length)
        The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
        The input is generated such that there is at least one query of type 2.
'''

from sortedcontainers import SortedList


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        barriers = SortedList()  # Sorted list to maintain barrier positions
        barriers.add(0)  # Add initial barrier at position 0

        # Process the add-barrier queries to populate the barriers list
        for query in queries:
            if query[0] == 1:
                it = query[1]
                barriers.add(it)

        holes = SortedList()  # Sorted list to maintain hole sizes
        holes.add(float('inf'))  # Initialize with an infinitely large hole
        hole2start = {float('inf'): barriers[-1]}

        # Calculate initial hole sizes based on the barriers
        for pos in range(len(barriers) - 1):
            start = barriers[pos]
            end = barriers[pos + 1]
            size = end - start
            if size:
                pos = holes.bisect_left(size)
                hole_size = holes[pos]
                if hole2start[hole_size] > start:
                    if hole_size > size:
                        holes.add(size)
                    hole2start[size] = start

        barriers.add(float('inf'))  # Add an infinite barrier at the end
 
        result = []
        # Process the queries in reverse order
        for query in reversed(queries):
            if query[0] == 1:  # If it's an add-barrier query
                it = query[1]
                pos = barriers.bisect_left(it)
                left = barriers[pos - 1]
                right = barriers[pos + 1]
                size = right - left

                hole_pos = holes.bisect_left(size)
                if hole2start[holes[hole_pos]] > left:
                    while hole_pos > 0 and hole2start[holes[hole_pos - 1]] > left:
                        del hole2start[holes[hole_pos - 1]]
                        del holes[hole_pos - 1]
                        hole_pos -= 1

                    hole2start[size] = left
                    if holes[hole_pos] != size:
                        holes.add(size)

                barriers.remove(it)
            else:  # If it's a check-hole query
                _, start, size = query
                hole_pos = holes.bisect_left(size)
                hole = holes[hole_pos]
                result.append(hole2start[hole] <= start - size)

        result.reverse()  # Reverse the result to match the original query order

        return result
