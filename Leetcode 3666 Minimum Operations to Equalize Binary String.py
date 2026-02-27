'''

Leetcode 3666 Minimum Operations to Equalize Binary String
 
You are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.
Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1. 

Example 1:
        Input: s = "110", k = 1
        Output: 1
        Explanation:
                There is one '0' in s.
                Since k = 1, we can flip it directly in one operation.

Example 2:
        Input: s = "0101", k = 3
        Output: 2
        Explanation: One optimal set of operations choosing k = 3 indices in each operation is:
                    Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
                    Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".
                    Thus, the minimum number of operations is 2.

Example 3:
Input: s = "101", k = 2
Output: -1
Explanation: Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.

Constraints:
        1 <= s.length <= 10​​​​​​​5
        s[i] is either '0' or '1'.
        1 <= k <= s.length
'''
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z0 = s.count('0')  # initial zeros

        if z0 == 0:
            return 0  # already all ones

        # sets of unvisited states (sorted lists)
        even = list(range(0, n + 1, 2))
        odd = list(range(1, n + 1, 2))
        visited = [False] * (n + 1)

        def erase_range(lst, L, R):
            """Erase all numbers in [L, R] from sorted list and return them."""
            l = bisect_left(lst, L)
            r = bisect_right(lst, R)
            result = lst[l:r]
            del lst[l:r]
            return result

        q = deque([(z0, 0)])
        visited[z0] = True

        while q:
            z, dist = q.popleft()
            i_min = max(0, k - (n - z))
            i_max = min(k, z)
            L = z + k - 2 * i_max
            R = z + k - 2 * i_min
            p = (z + k) % 2

            if p == 0:
                next_states = erase_range(even, max(0, L), min(n, R))
            else:
                next_states = erase_range(odd, max(0, L), min(n, R))

            for z2 in next_states:
                if not visited[z2]:
                    if z2 == 0:
                        return dist + 1
                    visited[z2] = True
                    q.append((z2, dist + 1))

        return -1
