# Solution 15: Toggle the i-th Bit

## Approach Explanation
XOR with a mask having only the i-th bit set. XOR with 1 flips the bit; XOR with 0 keeps it unchanged.

## Step-by-Step Logic
1. Create mask: `1 << i`.
2. Return `n ^ mask`.

## Complexity
- **Time Complexity:** O(1).
- **Space Complexity:** O(1).

## Code
```python
def toggle_bit(n, i):
    return n ^ (1 << i)
```
