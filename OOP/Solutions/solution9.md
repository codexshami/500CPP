# Solution 9: Stack using OOP

## Approach Explanation
Use a list internally with methods wrapping list operations.

## Step-by-Step Logic
1. __init__ with empty list.
2. push appends, pop removes last.
3. peek returns last, isEmpty checks length.

## Complexity
- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(N)

## Code
```python
class Stack:
    def __init__(self):
        self._items = []
    def push(self, item): self._items.append(item)
    def pop(self):
        if self.is_empty(): raise IndexError('Stack empty')
        return self._items.pop()
    def peek(self): return self._items[-1] if self._items else None
    def is_empty(self): return len(self._items) == 0
    def size(self): return len(self._items)
```
