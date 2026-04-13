# Solution 19: Find the Rightmost Set Bit

## Approach Explanation
Use `n & (-n)` to isolate the rightmost set bit. Then compute `log2` of the result to get the position, or count trailing zeros.

## Step-by-Step Logic
1. Isolate rightmost set bit: `rsb = n & (-n)`.
2. Find position: `log2(rsb) + 1` (1-indexed).

## Complexity
- **Time Complexity:** O(1).
- **Space Complexity:** O(1).

## Code
```python
import math

def rightmost_set_bit(n):
    rsb = n & (-n)
    return int(math.log2(rsb)) + 1
```
