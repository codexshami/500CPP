# Solution 2: LRU Cache

## Approach Explanation
Use an OrderedDict to maintain insertion order. Move accessed items to end.

## Step-by-Step Logic
1. Use OrderedDict for O(1) access and order management.
2. On get: move to end, return value.
3. On put: insert/update and evict oldest if over capacity.

## Complexity
- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(capacity)

## Code
```python
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```
