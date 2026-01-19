'''
295 Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle 
value, and the median is the mean of the two middle values.

        For example, for arr = [2,3,4], the median is 3.
        For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
        Input
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
        [[], [1], [2], [], [3], []]
        Output
        [null, null, null, 1.5, null, 2.0]

        Explanation
        MedianFinder medianFinder = new MedianFinder();
        medianFinder.addNum(1);    // arr = [1]
        medianFinder.addNum(2);    // arr = [1, 2]
        medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
        medianFinder.addNum(3);    // arr[1, 2, 3]
        medianFinder.findMedian(); // return 2.0
 

Constraints:
        -105 <= num <= 105
        There will be at least one element in the data structure before calling findMedian.
        At most 5 * 104 calls will be made to addNum and findMedian

'''

class MedianFinder:
  def __init__(self):
    self.maxHeap = []
    self.minHeap = []

  def addNum(self, num: int) -> None:
    if not self.maxHeap or num <= -self.maxHeap[0]:
      heapq.heappush(self.maxHeap, -num)
    else:
      heapq.heappush(self.minHeap, num)

    # Balance two heaps s.t.
    # |maxHeap| >= |minHeap| and |maxHeap| - |minHeap| <= 1
    if len(self.maxHeap) < len(self.minHeap):
      heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
    elif len(self.maxHeap) - len(self.minHeap) > 1:
      heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

  def findMedian(self) -> float:
    if len(self.maxHeap) == len(self.minHeap):
      return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
    return -self.maxHeap[0]


# Second solution
import heapq

class MedianFinder:
    """
    A data structure to efficiently calculate the median of a stream of numbers.
    """

    def __init__(self):
        """
        Initialize the MedianFinder with two heaps:
        - maxHeap: A max-heap to store the smaller half of the numbers.
        - minHeap: A min-heap to store the larger half of the numbers.
        """
        self.maxHeap = []  # Max-heap (invert values to simulate max-heap with heapq)
        self.minHeap = []  # Min-heap

    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.

        Parameters:
        num (int): The number to be added.
        """
        # Add to maxHeap if it's empty or the number is smaller than the maximum of maxHeap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)  # Use negative for max-heap simulation
        else:
            heapq.heappush(self.minHeap, num)

        # Balance the two heaps to ensure |maxHeap| >= |minHeap| and their size difference is <= 1
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        """
        Find the median of the numbers added so far.

        Returns:
        float: The median of the numbers.
        """
        # If the number of elements is even, return the average of the two middle elements
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        
        # If the number of elements is odd, return the middle element (max of maxHeap)
        return -self.maxHeap[0]


# Example of Implementation
if __name__ == "__main__":
    medianFinder = MedianFinder()
    numbers = [1, 2, 3, 4]
    for num in numbers:
        medianFinder.addNum(num)
        print(f"Added {num}, current median: {medianFinder.findMedian()}")  # Expected: 1, 1.5, 2, 2.5



