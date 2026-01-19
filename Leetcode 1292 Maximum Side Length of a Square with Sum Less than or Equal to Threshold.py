'''
Leetcode 1292 Maximum Side Length of a Square with Sum Less than or Equal to Threshold
 
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105


'''

class Solution:
    def isValid(self, pref, k, limit):
        n = len(pref)
        m = len(pref[0])

        for i in range(k - 1, n):
            for j in range(k - 1, m):
                x1 = i - k + 1
                y1 = j - k + 1

                total = pref[i][j]
                if x1 > 0:
                    total -= pref[x1 - 1][j]
                if y1 > 0:
                    total -= pref[i][y1 - 1]
                if x1 > 0 and y1 > 0:
                    total += pref[x1 - 1][y1 - 1]

                if total <= limit:
                    return True

        return False

    def maxSideLength(self, mat, threshold):
        n = len(mat)
        m = len(mat[0])

        pref = [row[:] for row in mat]

        # Row-wise prefix sum
        for i in range(n):
            for j in range(1, m):
                pref[i][j] += pref[i][j - 1]

        # Column-wise prefix sum
        for j in range(m):
            for i in range(1, n):
                pref[i][j] += pref[i - 1][j]

        low, high = 1, min(n, m)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if self.isValid(pref, mid, threshold):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
