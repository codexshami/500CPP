# Solution 14: Check if i-th Bit is Set

## Approach Explanation
Left-shift 1 by `i` positions to create a mask. AND with `n` — if the result is non-zero, the bit is set.

## Step-by-Step Logic
1. Create mask: `1 << i`.
2. Return `(n & mask) != 0`.

## Complexity
- **Time Complexity:** O(1).
- **Space Complexity:** O(1).

## Code
```python
def is_bit_set(n, i):
    return (n & (1 << i)) != 0
```
