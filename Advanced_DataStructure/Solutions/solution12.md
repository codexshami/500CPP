# Solution 12: Interval Tree

## Approach Explanation
Store intervals in a BST keyed by low endpoint, augmented with max endpoint in subtree.

## Step-by-Step Logic
1. Build BST on low endpoints.
2. Augment with max high endpoint.
3. Search: check overlap and navigate.

## Complexity
- **Time Complexity:** O(log N) per query
- **Space Complexity:** O(N)

## Code
```python
class IntervalNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max_high = high
        self.left = self.right = None

def insert_interval(root, low, high):
    if not root: return IntervalNode(low, high)
    if low < root.low:
        root.left = insert_interval(root.left, low, high)
    else:
        root.right = insert_interval(root.right, low, high)
    root.max_high = max(root.max_high, high)
    return root

def search_overlap(root, low, high):
    if not root: return None
    if root.low <= high and low <= root.high:
        return (root.low, root.high)
    if root.left and root.left.max_high >= low:
        return search_overlap(root.left, low, high)
    return search_overlap(root.right, low, high)
```
