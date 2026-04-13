# Solution 3: LFU Cache

## Approach Explanation
Use a min-frequency tracker with doubly linked lists per frequency level.

## Step-by-Step Logic
1. Track frequency of each key.
2. Maintain ordered dict per frequency.
3. On eviction, remove least frequent, then least recent.

## Complexity
- **Time Complexity:** O(1) per operation
- **Space Complexity:** O(capacity)

## Code
```python
from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.key_val = {}
        self.key_freq = {}
        self.freq_keys = defaultdict(OrderedDict)
        self.min_freq = 0
    def get(self, key):
        if key not in self.key_val:
            return -1
        self._update_freq(key)
        return self.key_val[key]
    def put(self, key, value):
        if self.cap <= 0: return
        if key in self.key_val:
            self.key_val[key] = value
            self._update_freq(key)
            return
        if len(self.key_val) >= self.cap:
            evict, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.key_val[evict]
            del self.key_freq[evict]
        self.key_val[key] = value
        self.key_freq[key] = 1
        self.freq_keys[1][key] = None
        self.min_freq = 1
    def _update_freq(self, key):
        freq = self.key_freq[key]
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.key_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = None
```
