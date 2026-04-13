# Solution 13: Linked List OOP

## Approach Explanation
Node stores value and next pointer. LinkedList manages head and operations.

## Step-by-Step Logic
1. Node has val and next.
2. LinkedList has head.
3. append, prepend, delete, display methods.

## Complexity
- **Time Complexity:** O(N) for operations
- **Space Complexity:** O(N)

## Code
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self): self.head = None
    def append(self, val):
        if not self.head: self.head = Node(val); return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = Node(val)
    def display(self):
        vals, curr = [], self.head
        while curr: vals.append(curr.val); curr = curr.next
        return vals
```
