# Solution 17: B-Tree Operations

## Approach Explanation
B-Tree of minimum degree t stores keys sorted in nodes with at most 2t-1 keys.

## Step-by-Step Logic
1. Search: BST-style search within nodes.
2. Insert: find leaf, split if full.
3. Split: move median up, create two children.

## Complexity
- **Time Complexity:** O(t * log_t(N))
- **Space Complexity:** O(N)

## Code
```python
class BTreeNode:
    def __init__(self, t, leaf=True):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == k:
            return True
        if self.leaf:
            return False
        return self.children[i].search(k)
```
