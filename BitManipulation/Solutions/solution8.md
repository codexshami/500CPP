# Solution 8: Sum of Two Integers Without Arithmetic Operators

## Approach Explanation
Use XOR for addition without carry, AND + left shift for carry. Repeat until carry is zero. Handle negative numbers with 32-bit masking in Python.

## Step-by-Step Logic
1. Use a mask `0xFFFFFFFF` to simulate 32-bit integers.
2. While `b != 0`: compute `carry = (a & b) << 1`, `a = a ^ b`, `b = carry`. Apply mask.
3. If `a > 0x7FFFFFFF`, convert to negative using `~(a ^ mask)`.

## Complexity
- **Time Complexity:** O(1) — at most 32 iterations.
- **Space Complexity:** O(1).

## Code
```python
def get_sum(a, b):
    MASK = 0xFFFFFFFF
    MAX = 0x7FFFFFFF
    
    while b & MASK:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    
    # If b is 0, return a (handle negative)
    return (a & MASK) if a > MAX else a
```
