# Solution 6: Fenwick Tree

## Approach Explanation
Use a BIT array where each index stores a partial sum based on its lowest set bit.

## Step-by-Step Logic
1. Initialize BIT of size n+1.
2. Update: add delta at index, propagate using i += i&(-i).
3. Query: sum using i -= i&(-i).

## Complexity
- **Time Complexity:** O(log N) per operation
- **Space Complexity:** O(N)

## Code
```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    def range_query(self, l, r):
        return self.query(r) - (self.query(l-1) if l > 0 else 0)
```
