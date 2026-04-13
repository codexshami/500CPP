# Solution 9: Skip List

## Approach Explanation
Probabilistic data structure with multiple levels of linked lists for O(log n) search.

## Step-by-Step Logic
1. Each node has random height.
2. Search from top level down.
3. Insert at correct position with random levels.

## Complexity
- **Time Complexity:** O(log N) expected
- **Space Complexity:** O(N log N)

## Code
```python
import random
class SkipNode:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)
class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(-1, max_level)
        self.level = 0
    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl
    def search(self, val):
        curr = self.header
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr and curr.val == val
```
