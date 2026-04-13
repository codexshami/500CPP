# Solution 10: Bloom Filter

## Approach Explanation
Use multiple hash functions to set bits in a bit array. Check all bits for membership.

## Step-by-Step Logic
1. Initialize bit array of size m.
2. Add: compute k hash positions, set bits.
3. Contains: check if all k bit positions are set.

## Complexity
- **Time Complexity:** O(k) per operation
- **Space Complexity:** O(m)

## Code
```python
class BloomFilter:
    def __init__(self, size=1000, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [False] * size
    def _hashes(self, item):
        positions = []
        for i in range(self.num_hashes):
            h = hash(str(item) + str(i)) % self.size
            positions.append(h)
        return positions
    def add(self, item):
        for pos in self._hashes(item):
            self.bits[pos] = True
    def contains(self, item):
        return all(self.bits[pos] for pos in self._hashes(item))
```
