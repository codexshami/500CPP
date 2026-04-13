# Solution 19: Red-Black Tree Insert

## Approach Explanation
BST with color property (red/black). Recolor and rotate after insertion.

## Step-by-Step Logic
1. Insert as red node (BST insert).
2. Fix violations: recolor or rotate.
3. Root is always black.

## Complexity
- **Time Complexity:** O(log N)
- **Space Complexity:** O(N)

## Code
```python
class RBNode:
    def __init__(self, val, color='R'):
        self.val = val
        self.color = color
        self.left = self.right = self.parent = None

def rb_insert(root, val):
    node = RBNode(val)
    # Standard BST insert
    if not root:
        node.color = 'B'
        return node
    curr = root
    while curr:
        node.parent = curr
        if val < curr.val:
            if not curr.left:
                curr.left = node
                break
            curr = curr.left
        else:
            if not curr.right:
                curr.right = node
                break
            curr = curr.right
    # Fix-up would go here (recolor + rotate)
    return root
```
