# Solution 7: Disjoint Set Union

## Approach Explanation
Use parent array with path compression and union by rank for near O(1) operations.

## Step-by-Step Logic
1. Find with path compression: point directly to root.
2. Union by rank: attach smaller tree under larger.

## Complexity
- **Time Complexity:** O(alpha(N)) amortized
- **Space Complexity:** O(N)

## Code
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True
    def connected(self, x, y):
        return self.find(x) == self.find(y)
```
