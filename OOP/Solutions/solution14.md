# Solution 14: Iterator Pattern

## Approach Explanation
Implement __iter__ and __next__ for a BST in-order traversal using a stack.

## Step-by-Step Logic
1. Initialize stack with leftmost path.
2. __next__ pops, processes, pushes right subtree.
3. StopIteration when stack empty.

## Complexity
- **Time Complexity:** O(1) amortized per next
- **Space Complexity:** O(H)

## Code
```python
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    def __iter__(self): return self
    def __next__(self):
        if not self.stack: raise StopIteration
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val
    def has_next(self): return len(self.stack) > 0
```
