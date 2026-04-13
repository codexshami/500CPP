# Solution 7: Hamming Distance

## Approach Explanation
XOR the two numbers — the result has 1s exactly where the bits differ. Count the set bits in the XOR result.

## Step-by-Step Logic
1. Compute `xor = x ^ y`.
2. Count set bits in `xor` using Brian Kernighan's algorithm.

## Complexity
- **Time Complexity:** O(1) — at most 31 bits.
- **Space Complexity:** O(1).

## Code
```python
def hamming_distance(x, y):
    xor = x ^ y
    count = 0
    while xor:
        xor &= (xor - 1)
        count += 1
    return count
```
