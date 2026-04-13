# Solution 16: Splay Tree

## Approach Explanation
Move accessed nodes to root using zig, zig-zig, and zig-zag rotations.

## Step-by-Step Logic
1. On access, splay the node to root.
2. Zig: single rotation.
3. Zig-zig/zig-zag: double rotations.

## Complexity
- **Time Complexity:** O(log N) amortized
- **Space Complexity:** O(N)

## Code
```python
class SplayNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.parent = None

def rotate(x):
    p = x.parent
    if not p: return
    g = p.parent
    if p.left == x:
        p.left = x.right
        if x.right: x.right.parent = p
        x.right = p
    else:
        p.right = x.left
        if x.left: x.left.parent = p
        x.left = p
    p.parent = x
    x.parent = g
    if g:
        if g.left == p: g.left = x
        else: g.right = x
```
