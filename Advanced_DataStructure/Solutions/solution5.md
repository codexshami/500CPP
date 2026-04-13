# Solution 5: Segment Tree - Range Min

## Approach Explanation
Same as range sum but store minimum instead.

## Step-by-Step Logic
1. Build with min operation.
2. Query returns minimum in range.
3. Update leaf and propagate.

## Complexity
- **Time Complexity:** O(log N) per operation
- **Space Complexity:** O(N)

## Code
```python
class MinSegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])
    def query(self, l, r):
        res = float('inf')
        l += self.n; r += self.n
        while l < r:
            if l & 1: res = min(res, self.tree[l]); l += 1
            if r & 1: r -= 1; res = min(res, self.tree[r])
            l //= 2; r //= 2
        return res
```
