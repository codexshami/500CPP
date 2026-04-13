# Solution 8: Min-Max Heap

## Approach Explanation
Maintain two heaps: a min-heap and a max-heap with cross-references.

## Step-by-Step Logic
1. Keep a min-heap and max-heap in sync.
2. Insert into both.
3. Delete from one and mark as deleted in the other.

## Complexity
- **Time Complexity:** O(log N) insert/delete, O(1) find
- **Space Complexity:** O(N)

## Code
```python
import heapq
class MinMaxHeap:
    def __init__(self):
        self.min_h = []
        self.max_h = []
        self.removed = set()
        self.counter = 0
    def insert(self, val):
        entry = (val, self.counter)
        self.counter += 1
        heapq.heappush(self.min_h, entry)
        heapq.heappush(self.max_h, (-val, entry[1]))
    def _clean_min(self):
        while self.min_h and self.min_h[0][1] in self.removed:
            heapq.heappop(self.min_h)
    def _clean_max(self):
        while self.max_h and self.max_h[0][1] in self.removed:
            heapq.heappop(self.max_h)
    def find_min(self):
        self._clean_min()
        return self.min_h[0][0]
    def find_max(self):
        self._clean_max()
        return -self.max_h[0][0]
```
