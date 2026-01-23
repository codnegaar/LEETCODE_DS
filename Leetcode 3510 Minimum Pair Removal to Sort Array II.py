'''

Leetcode 3510 Minimum Pair Removal to Sort Array II
 
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one. Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.
An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
 

Example 1:
Input: nums = [5,2,3,1]
        Output: 2
        Explanation:
                    The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
                    The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
                    The array nums became non-decreasing in two operations.

Example 2:
        Input: nums = [1,2,2]
        Output: 0
        Explanation: The array nums is already sorted.

Constraints:
        1 <= nums.length <= 105
        -109 <= nums[i] <= 109


'''

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        arr = [int(x) for x in nums]
        removed = [False] * n
        heap = []
        asc = 0
        for i in range(1, n):
            heapq.heappush(heap, (arr[i - 1] + arr[i], i - 1))
            if arr[i] >= arr[i - 1]:
                asc += 1
        if asc == n - 1:
            return 0

        rem = n
        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 for i in range(n)]

        while rem > 1:
            if not heap:
                break
            sumv, left = heapq.heappop(heap)
            right = nxt[left]
            if right >= n or removed[left] or removed[right] or arr[left] + arr[right] != sumv:
                continue

            pre = prev[left]
            after = nxt[right]

            if arr[left] <= arr[right]:
                asc -= 1
            if pre != -1 and arr[pre] <= arr[left]:
                asc -= 1
            if after != n and arr[right] <= arr[after]:
                asc -= 1

            arr[left] += arr[right]
            removed[right] = True
            rem -= 1

            if pre != -1:
                heapq.heappush(heap, (arr[pre] + arr[left], pre))
                if arr[pre] <= arr[left]:
                    asc += 1
            else:
                prev[left] = -1

            if after != n:
                prev[after] = left
                nxt[left] = after
                heapq.heappush(heap, (arr[left] + arr[after], left))
                if arr[left] <= arr[after]:
                    asc += 1
            else:
                nxt[left] = n

            if asc == rem - 1:
                return n - rem

        return n
