# Solution 10: Closest Pair of Points (Brute)

## Approach Explanation
Check all pairs and track the minimum distance.

## Step-by-Step Logic
1. Double loop over all pairs.
2. Compute distance for each pair.
3. Track minimum.

## Complexity
- **Time Complexity:** O(N²)
- **Space Complexity:** O(1)

## Code
```python
import math
def closest_pair_brute(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
            min_dist = min(min_dist, d)
    return min_dist
```
