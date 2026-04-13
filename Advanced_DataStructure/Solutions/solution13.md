# Solution 13: Sparse Table

## Approach Explanation
Precompute answers for all ranges of length 2^k. Answer queries by combining two overlapping ranges.

## Step-by-Step Logic
1. Build table[i][j] = min of range starting at i with length 2^j.
2. Query: combine two overlapping ranges of appropriate power of 2.

## Complexity
- **Time Complexity:** O(N log N) build, O(1) query
- **Space Complexity:** O(N log N)

## Code
```python
import math
class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = int(math.log2(n)) + 1
        self.table = [[0]*n for _ in range(k)]
        self.table[0] = arr[:]
        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.table[j][i] = min(self.table[j-1][i], self.table[j-1][i + (1 << (j-1))])
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i//2] + 1
    def query(self, l, r):
        j = self.log[r - l + 1]
        return min(self.table[j][l], self.table[j][r - (1 << j) + 1])
```
