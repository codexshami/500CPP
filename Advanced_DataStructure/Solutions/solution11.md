# Solution 11: Order Statistics Tree

## Approach Explanation
Augment BST nodes with subtree sizes to support select and rank.

## Step-by-Step Logic
1. Each node stores subtree size.
2. Select(k): use sizes to navigate.
3. Rank(x): count nodes less than x.

## Complexity
- **Time Complexity:** O(log N) average
- **Space Complexity:** O(N)

## Code
```python
class OSTNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.size = 1

def insert(root, val):
    if not root: return OSTNode(val)
    root.size += 1
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def select(root, k):
    left_size = root.left.size if root.left else 0
    if k == left_size + 1: return root.val
    if k <= left_size: return select(root.left, k)
    return select(root.right, k - left_size - 1)
```
