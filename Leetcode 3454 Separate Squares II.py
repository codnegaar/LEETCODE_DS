'''

Leetcode 3454 Separate Squares II
 
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.
Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.
Answers within 10-5 of the actual answer will be accepted.
Note: Squares may overlap. Overlapping areas should be counted only once in this version.

Example 1:
          Input: squares = [[0,0,1],[2,2,1]]
          Output: 1.00000
          Explanation: Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

Example 2:
          Input: squares = [[0,0,2],[1,1,1]]
          Output: 1.00000
          Explanation: Since the blue square overlaps with the red square, it will not be counted again. Thus, the line y = 1 splits the squares into two equal parts.
                 
Constraints:
          1 <= squares.length <= 5 * 104
          squares[i] = [xi, yi, li]
          squares[i].length == 3
          0 <= xi, yi <= 109
          1 <= li <= 109
          The total area of all the squares will not exceed 1015.
'''

class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs # sorted x coordinates
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)
    
    # be careful when you are reading over, we use right + 1 instead of right.
    # make sure you understand why.
    def update(self, qleft, qright, qval, left, right, pos):
        if self.xs[right+1] <= qleft or self.xs[left] >= qright: # no overlap
            return
        if qleft <= self.xs[left] and self.xs[right+1] <= qright: # full overlap
            self.count[pos] += qval
        else: # partial overlap
            mid = (left + right) // 2
            self.update(qleft, qright, qval, left, mid, pos*2 + 1)
            self.update(qleft, qright, qval, mid+1, right, pos*2 + 2)

        if self.count[pos] > 0:
            self.covered[pos] = self.xs[right+1] - self.xs[left]
        else:
            if left == right:
                self.covered[pos] = 0
            else:
                self.covered[pos] = self.covered[pos*2 + 1] + self.covered[pos*2 + 2]
    
    def query(self):
        return self.covered[0]

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs_set = set()
        for x, y, l in squares:
            events.append((y, 1, x, x+l)) 
            events.append((y+l, -1, x, x+l))
            xs_set.update([x, x + l])
        xs = sorted(xs_set)
        
        seg_tree = SegmentTree(xs)
        events.sort()
        
        # first sweep: compute total union area.
        total_area = 0.0
        prev_y = events[0][0]
        for y, start, xl, xr in events:
            total_area += seg_tree.query() * (y - prev_y)
            seg_tree.update(xl, xr, start, 0, seg_tree.n - 1, 0)
            prev_y = y
        
        # second sweep: find the minimal y where the area below equals half_area.
        seg_tree = SegmentTree(xs)  # reinitialize segment tree
        curr_area = 0.0
        prev_y = events[0][0]
        for y, start, xl, xr in events:
            combined_width = seg_tree.query()
            if curr_area + combined_width * (y - prev_y) >= total_area / 2.0:
                # curr_area + (combined_width * optimal_height_diff) = total_area / 2
                return prev_y + (total_area / 2.0 - curr_area) / combined_width
            curr_area += combined_width * (y - prev_y)
            seg_tree.update(xl, xr, start, 0, seg_tree.n - 1, 0)
            prev_y = y
