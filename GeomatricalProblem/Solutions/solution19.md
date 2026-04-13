# Solution 19: Lattice Points on Line Segment

## Approach Explanation
Count = GCD(|x2-x1|, |y2-y1|) + 1.

## Step-by-Step Logic
1. Compute absolute differences.
2. Find GCD.
3. Return GCD + 1.

## Complexity
- **Time Complexity:** O(log(max(dx,dy)))
- **Space Complexity:** O(1)

## Code
```python
import math
def lattice_points(x1, y1, x2, y2):
    return math.gcd(abs(x2-x1), abs(y2-y1)) + 1
```
