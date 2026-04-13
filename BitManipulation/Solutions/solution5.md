# Solution 5: Reverse Bits

## Approach Explanation
Process each bit from right to left, shifting the result left and adding the current bit. Repeat 32 times.

## Step-by-Step Logic
1. Initialize `result = 0`.
2. For 32 iterations: shift `result` left by 1, add `n & 1`, shift `n` right by 1.
3. Return `result`.

## Complexity
- **Time Complexity:** O(1) — always 32 iterations.
- **Space Complexity:** O(1).

## Code
```python
def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```
