# Solution 15: Treap

## Approach Explanation
Combine BST (by value) and heap (by random priority) properties.

## Step-by-Step Logic
1. Each node has value and random priority.
2. Insert: BST insert then rotate to maintain heap.
3. Split and merge for efficient operations.

## Complexity
- **Time Complexity:** O(log N) expected
- **Space Complexity:** O(N)

## Code
```python
import random
class TreapNode:
    def __init__(self, val):
        self.val = val
        self.priority = random.random()
        self.left = self.right = None

def split(node, val):
    if not node: return None, None
    if node.val <= val:
        left, node.right = split(node.right, val)
        return node, left
    else:
        node.left, right = split(node.left, val)
        return right, node

def merge(left, right):
    if not left or not right: return left or right
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    right.left = merge(left, right.left)
    return right
```
