# Solution 20: Maximum Points on a Line

## Approach Explanation
For each point, compute slopes to all other points using a hash map. Track the maximum.

## Step-by-Step Logic
1. For each point, compute slope (as fraction) to all others.
2. Use a dictionary to count collinear points.
3. Track global maximum.

## Complexity
- **Time Complexity:** O(N²)
- **Space Complexity:** O(N)

## Code
```python
from collections import defaultdict
import math

def max_points(points):
    if len(points) <= 2:
        return len(points)
    
    max_count = 2
    for i in range(len(points)):
        slopes = defaultdict(int)
        for j in range(len(points)):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = math.gcd(abs(dx), abs(dy))
            if g:
                dx, dy = dx//g, dy//g
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0:
                dy = abs(dy)
            slopes[(dx, dy)] += 1
        if slopes:
            max_count = max(max_count, max(slopes.values()) + 1)
    return max_count
```
