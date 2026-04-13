# Solution 2: Number of 1 Bits (Hamming Weight)

## Approach Explanation
Use Brian Kernighan's algorithm: `n & (n-1)` drops the lowest set bit. Count how many times we can do this before n becomes 0.

## Step-by-Step Logic
1. Initialize `count = 0`.
2. While `n > 0`: set `n = n & (n - 1)`, increment `count`.
3. Return `count`.

## Complexity
- **Time Complexity:** O(k) where k is the number of set bits.
- **Space Complexity:** O(1).

## Code
```python
def hamming_weight(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
```
