# Solution 5: Distance Between Two Points

## Approach Explanation
Use the Euclidean distance formula: √((x2-x1)² + (y2-y1)²).

## Step-by-Step Logic
1. Compute differences.
2. Square, sum, take square root.

## Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Code
```python
import math
def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
```
