# Solution 3: Power of Two

## Approach Explanation
A power of two has exactly one set bit. So `n & (n - 1)` must be 0, and `n` must be positive.

## Step-by-Step Logic
1. Check if `n > 0` and `n & (n - 1) == 0`.

## Complexity
- **Time Complexity:** O(1).
- **Space Complexity:** O(1).

## Code
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```
