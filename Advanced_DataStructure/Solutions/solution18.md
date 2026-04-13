# Solution 18: AVL Tree

## Approach Explanation
BST with balance factor (height difference <= 1). Rotate after inserts/deletes.

## Step-by-Step Logic
1. Track height at each node.
2. After insert, check balance factor.
3. Rotate (LL, RR, LR, RL) to rebalance.

## Complexity
- **Time Complexity:** O(log N)
- **Space Complexity:** O(N)

## Code
```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def insert_avl(root, val):
    if not root: return AVLNode(val)
    if val < root.val: root.left = insert_avl(root.left, val)
    else: root.right = insert_avl(root.right, val)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and val < root.left.val: return right_rotate(root)
    # ... other rotation cases
    return root
```
