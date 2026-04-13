# Solution 4: Segment Tree - Range Sum

## Approach Explanation
Build a tree where each node stores sum of a range. Update and query in O(log N).

## Step-by-Step Logic
1. Build tree bottom-up.
2. Update: modify leaf, propagate up.
3. Query: combine results from relevant segments.

## Complexity
- **Time Complexity:** O(log N) per operation
- **Space Complexity:** O(N)

## Code
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    def query(self, l, r):  # [l, r)
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1: res += self.tree[l]; l += 1
            if r & 1: r -= 1; res += self.tree[r]
            l //= 2; r //= 2
        return res
```
