# Solution 19: Queue using Two Stacks

## Approach Explanation
Use two stacks: one for enqueue, one for dequeue. Transfer elements lazily.

## Step-by-Step Logic
1. Push to stack1 for enqueue.
2. For dequeue, if stack2 empty, transfer all from stack1.
3. Pop from stack2.

## Complexity
- **Time Complexity:** O(1) amortized
- **Space Complexity:** O(N)

## Code
```python
class QueueTwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, val): self.s1.append(val)
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2: raise IndexError('Queue empty')
        return self.s2.pop()
    def is_empty(self): return not self.s1 and not self.s2
```
