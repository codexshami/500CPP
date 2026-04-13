# Solution 18: Minimum Flips to Make a OR b Equal to c

## Approach Explanation
Check each bit position. If c's bit is 1, at least one of a or b must have 1 (if neither does, flip 1). If c's bit is 0, both a and b must be 0 (flip each 1-bit).

## Step-by-Step Logic
1. For each bit position (0 to 30).
2. If c's bit is 0: add number of 1-bits in a and b at this position.
3. If c's bit is 1: if both a and b have 0, add 1 flip.

## Complexity
- **Time Complexity:** O(1) — 31 bits.
- **Space Complexity:** O(1).

## Code
```python
def min_flips(a, b, c):
    flips = 0
    for i in range(31):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        bit_c = (c >> i) & 1
        
        if bit_c == 0:
            flips += bit_a + bit_b
        else:
            if bit_a == 0 and bit_b == 0:
                flips += 1
    
    return flips
```
