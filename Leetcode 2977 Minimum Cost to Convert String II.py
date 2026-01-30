'''
Leetcode 2977 Minimum Cost to Convert String II
 
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English characters. You are also given two 0-indexed string arrays 
original and changed, and an integer array cost, where cost[i] represents the cost of converting the string original[i] to the string changed[i].

You start with the string source. In one operation, you can pick a substring x from the string, and change it to y at a cost of z if there exists any index j such that 
cost[j] == z, original[j] == x, and changed[j] == y. You are allowed to do any number of operations, but any pair of operations must satisfy either of these two conditions:
The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In other words, the indices picked in both operations are disjoint.
The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other words, the indices picked in both operations are identical.
Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

Example 1:
        Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
        Output: 28
        Explanation: To convert "abcd" to "acbe", do the following operations:
        - Change substring source[1..1] from "b" to "c" at a cost of 5.
        - Change substring source[2..2] from "c" to "e" at a cost of 1.
        - Change substring source[2..2] from "e" to "b" at a cost of 2.
        - Change substring source[3..3] from "d" to "e" at a cost of 20.
        The total cost incurred is 5 + 1 + 2 + 20 = 28. 
        It can be shown that this is the minimum possible cost.

Example 2:        
        Input: source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
        Output: 9
        Explanation: To convert "abcdefgh" to "acdeeghh", do the following operations:
        - Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
        - Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
        - Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
        The total cost incurred is 1 + 3 + 5 = 9.
        It can be shown that this is the minimum possible cost.

Example 3:
        Input: source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]
        Output: -1
        Explanation: It is impossible to convert "abcdefgh" to "addddddd".
        If you select substring source[1..3] as the first operation to change "abcdefgh" to "adddefgh", you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
        If you select substring source[3..7] as the first operation to change "abcdefgh" to "abcddddd", you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.
         

Constraints:

1 <= source.length == target.length <= 1000
source, target consist only of lowercase English characters.
1 <= cost.length == original.length == changed.length <= 100
1 <= original[i].length == changed[i].length <= source.length
original[i], changed[i] consist only of lowercase English characters.
original[i] != changed[i]
1 <= cost[i] <= 106

'''

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def djikstra(node):
            minhpq = [(0, node)]         # min heap storing (cost, node)
            min_cost_map = dict()        # stores the {node: cost}

            while minhpq:
                cost, curr = heappop(minhpq)

                # pass
                if curr in min_cost_map:
                    continue

                # mark as seen
                min_cost_map[curr] = cost

                # search for next candidates
                for neigh, neigh_cost in adj[curr]:
                    new_cost = cost + neigh_cost
                    heappush(minhpq, (new_cost, neigh))

            return min_cost_map

        def dfs(i):
            nonlocal n, lengths

            # base
            if i >= n:
                return 0

            # seen before
            if i in memo:
                return memo[i]

            # case1; 
            res = float('inf')

            # recur to index i + 1 if same value for ith index in source and target
            if source[i] == target[i]:
                res = dfs(i + 1)

            # recur on subset of source and target based on valid size length
            for size in lengths:
                # slice source and target string
                sub_s = source[i: i + size]
                sub_t = target[i: i + size]

                # run bfs for sub_s if substring sub_s 
                # does not exist in min_cost_maps
                if sub_s not in min_cost_maps:
                    min_cost_maps[sub_s] = djikstra(sub_s)    # append results to min_cost_maps

                # recur after sub_s if sub_t exist in min_cost_maps[sub_s]
                if sub_t in min_cost_maps[sub_s]:
                    cost = min_cost_maps[sub_s][sub_t]        # pull out cost from sub_s -> sub_t
                    new_i = i + size                          # new index after slicing
                    solution = cost + dfs(new_i)   

                    # compare  
                    res = min(res, solution)
                
            # allocate final res
            memo[i] = res

            return memo[i]

        # get the lenth of source strings
        lengths = set()

        # 1. build the directed graph
        adj = defaultdict(list)
        for src, des, c in zip(original, changed, cost):
            adj[src] += [(des, c)]
            lengths.add(len(src))

        # 2. stores min cost for each pair of (src, des)
        min_cost_maps = {ch: djikstra(ch) for ch in set(source)}

        n = len(source)

        # memo[i] := minimum cost to convert string/substring source to string/substring target starting at index i
        memo = dict()

        # 3. run dp starting at index 0 of source
        res = dfs(0)

        # 4. return -1 if dp result is inf
        return -1 if res == float('inf') else res
